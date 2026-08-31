"""
Construye el Manual de Bolsillo en dos formatos a partir de los archivos .md:

  1. sketchy.html   -> version para el Artifact de Claude (todo en un archivo,
                       imagenes incrustadas, limitada a ~16 MB en total).
  2. docs/          -> version para GitHub Pages (imagenes como archivos
                       normales junto al HTML, sin limite de tamano, mas
                       nitidas y con cache del navegador).

Uso:  python construir.py

Para anadir un Sketchy nuevo:
  1. Crea su archivo .md en la carpeta de su Parte.
  2. Guarda sus dos imagenes en la carpeta "imagenes":
        <nombre-del-md>-mapa.png    (el dibujo con los numeros)
        <nombre-del-md>-texto.png   (la hoja de explicaciones)
     Sirve .png, .jpg, .jpeg o .webp indistintamente.
  3. Vuelve a ejecutar este script.
"""

import base64
import io
import json
import re
import shutil
from pathlib import Path

BASE = Path(__file__).parent
IMGS = BASE / "imagenes"
DOCS = BASE / "docs"

PARTES = [
    ("01-gram-positivas", "Gram-positivas", "gp"),
    ("02-gram-negativas", "Gram-negativas", "gn"),
    ("03-rickettsias", "Rickettsias", "rk"),
    ("04-virus", "Virus", "vi"),
    ("05-patologia-gi", "Patología GI", "pa"),
    ("06-hematologia", "Hematología", "he"),
    ("07-farmacologia", "Farmacología", "fa"),
    ("08-neurologia", "Neurología", "ne"),
    ("09-neumologia", "Neumología", "nu"),
    ("10-inmunologia", "Inmunología", "im"),
    ("11-ginecologia", "Ginecología", "gi"),
    ("12-parasitologia", "Parasitología", "pr"),
]

PASOS = [("🎨", "ver"), ("💡", "clinica"), ("🧠", "sketchy"), ("📜", "literal")]

EXTENSIONES = (".png", ".jpg", ".jpeg", ".webp", ".PNG", ".JPG", ".JPEG", ".WEBP")

# --- limites solo para la version Artifact (sketchy.html) ---
PRESUPUESTO_ARTIFACT = 13_200_000
TOPE_MAX_ARTIFACT = 620_000
TOPE_MIN_ARTIFACT = 90_000

# --- calidad fija para la version web (docs/), sin limite de peso total ---
ANCHO_WEB = 2400
CALIDAD_WEB = 88


def buscar_imagen(slug, sufijo):
    for ext in EXTENSIONES:
        p = IMGS / f"{slug}-{sufijo}{ext}"
        if p.is_file():
            return p
    return None


def cargar_imagen(ruta):
    from PIL import Image
    img = Image.open(ruta)
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    return img


def comprimir_data_uri(ruta, tope_bytes):
    """Para el Artifact: data URI webp que quepa dentro de tope_bytes."""
    try:
        img = cargar_imagen(ruta)
    except ImportError:
        return "data:image/png;base64," + base64.b64encode(ruta.read_bytes()).decode()

    if tope_bytes >= 400_000:
        ancho_max = 2400
    elif tope_bytes >= 250_000:
        ancho_max = 2000
    elif tope_bytes >= 160_000:
        ancho_max = 1700
    else:
        ancho_max = 1400

    if img.width > ancho_max:
        alto = round(img.height * ancho_max / img.width)
        img = img.resize((ancho_max, alto), Image.LANCZOS)

    mejor = None
    for calidad in (90, 84, 78, 72, 66, 60, 54, 48, 42, 36, 30):
        buf = io.BytesIO()
        img.save(buf, format="WEBP", quality=calidad, method=6)
        mejor = buf.getvalue()
        if len(mejor) * 4 / 3 <= tope_bytes:
            break

    return "data:image/webp;base64," + base64.b64encode(mejor).decode()


def exportar_archivo_web(ruta, destino):
    """Para GitHub Pages: guarda un .webp de alta calidad como archivo suelto."""
    img = cargar_imagen(ruta)
    if img.width > ANCHO_WEB:
        alto = round(img.height * ANCHO_WEB / img.width)
        img = img.resize((ANCHO_WEB, alto), Image.LANCZOS)
    img.save(destino, format="WEBP", quality=CALIDAD_WEB, method=6)
    return destino.stat().st_size


def limpiar(texto):
    lineas = []
    for linea in texto.strip().split("\n"):
        linea = linea.strip()
        if linea.startswith("→"):
            linea = linea[1:].strip()
        if linea:
            lineas.append(linea)
    return "\n".join(lineas)


def leer_tema(ruta):
    crudo = ruta.read_text(encoding="utf-8")
    bloques = [b.strip() for b in crudo.split("\n---\n")]

    m = re.search(r"^#\s+(.+)$", bloques[0], re.MULTILINE)
    titulo = m.group(1).strip() if m else ruta.stem
    titulo = re.sub(r"^[^\w(]+", "", titulo).strip()

    items = []
    for bloque in bloques[1:]:
        if "🔢" not in bloque:
            continue
        m = re.search(r"🔢\s*(\S+)\.?\s*(.*)", bloque)
        if not m:
            continue
        item = {"n": m.group(1).rstrip("."), "nombre": m.group(2).strip()}
        for emoji, clave in PASOS:
            patron = rf"{emoji}[^\n]*\n(.*?)(?=\n\s*(?:🎨|💡|🧠|📜)|\Z)"
            m2 = re.search(patron, bloque, re.DOTALL)
            item[clave] = limpiar(m2.group(1)) if m2 else ""
        items.append(item)

    return {
        "slug": ruta.stem,
        "titulo": titulo,
        "items": items,
        "_mapa": buscar_imagen(ruta.stem, "mapa"),
        "_texto": buscar_imagen(ruta.stem, "texto"),
    }


def recolectar():
    partes, n_img = [], 0
    for carpeta, nombre, codigo in PARTES:
        d = BASE / carpeta
        if not d.is_dir():
            continue
        temas = []
        for f in sorted(d.glob("*.md")):
            t = leer_tema(f)
            if not t["items"]:
                continue
            n_img += bool(t["_mapa"]) + bool(t["_texto"])
            temas.append(t)
        if temas:
            partes.append({"nombre": nombre, "codigo": codigo, "temas": temas})
    return partes, n_img


def render_html(plantilla, partes, n_temas, n_items):
    datos = json.dumps(partes, ensure_ascii=False, separators=(",", ":"))
    return (plantilla
            .replace("/*DATOS*/null", datos)
            .replace("{{N_TEMAS}}", str(n_temas))
            .replace("{{N_ITEMS}}", str(n_items)))


def construir():
    IMGS.mkdir(exist_ok=True)
    partes, n_img = recolectar()
    n_temas = sum(len(p["temas"]) for p in partes)
    n_items = sum(len(t["items"]) for p in partes for t in p["temas"])
    plantilla = (BASE / "plantilla.html").read_text(encoding="utf-8")

    faltan = [t["slug"] for p in partes for t in p["temas"] if not (t["_mapa"] and t["_texto"])]

    # ========== 1) VERSION ARTIFACT (sketchy.html, base64, con presupuesto) ==========
    tope = max(TOPE_MIN_ARTIFACT, min(TOPE_MAX_ARTIFACT, PRESUPUESTO_ARTIFACT // n_img)) if n_img else TOPE_MAX_ARTIFACT

    partes_artifact = json.loads(json.dumps(partes, default=lambda o: None))  # copia sin los Path
    for p_orig, p_copia in zip(partes, partes_artifact):
        for t_orig, t_copia in zip(p_orig["temas"], p_copia["temas"]):
            t_copia.pop("_mapa", None); t_copia.pop("_texto", None)
            if t_orig["_mapa"]:
                t_copia["mapa"] = comprimir_data_uri(t_orig["_mapa"], tope)
            if t_orig["_texto"]:
                t_copia["texto"] = comprimir_data_uri(t_orig["_texto"], tope)

    salida_artifact = render_html(plantilla, partes_artifact, n_temas, n_items)
    destino_artifact = BASE / "sketchy.html"
    destino_artifact.write_text(salida_artifact, encoding="utf-8")
    mb_artifact = destino_artifact.stat().st_size / 1_048_576

    # ========== 2) VERSION WEB (docs/, archivos sueltos, sin limite) ==========
    docs_img = DOCS / "imagenes"
    docs_img.mkdir(parents=True, exist_ok=True)

    partes_web = json.loads(json.dumps(partes, default=lambda o: None))
    peso_web = 0
    for p_orig, p_copia in zip(partes, partes_web):
        for t_orig, t_copia in zip(p_orig["temas"], p_copia["temas"]):
            t_copia.pop("_mapa", None); t_copia.pop("_texto", None)
            if t_orig["_mapa"]:
                destino = docs_img / f"{t_orig['slug']}-mapa.webp"
                peso_web += exportar_archivo_web(t_orig["_mapa"], destino)
                t_copia["mapa"] = f"imagenes/{destino.name}"
            if t_orig["_texto"]:
                destino = docs_img / f"{t_orig['slug']}-texto.webp"
                peso_web += exportar_archivo_web(t_orig["_texto"], destino)
                t_copia["texto"] = f"imagenes/{destino.name}"

    salida_web = render_html(plantilla, partes_web, n_temas, n_items)
    (DOCS / "index.html").write_text(salida_web, encoding="utf-8")

    print(f"Artifact -> sketchy.html")
    print(f"  {n_img} imagenes | {tope // 1000} KB c/u | peso total: {mb_artifact:.2f} MB de 16 MB")
    if mb_artifact > 15:
        print("  AVISO: cerca del limite. Baja PRESUPUESTO_ARTIFACT.")

    print(f"\nWeb (GitHub Pages) -> docs/")
    print(f"  {n_img} imagenes a {ANCHO_WEB}px | peso imagenes: {peso_web / 1_048_576:.1f} MB (sin limite)")

    print(f"\n{len(partes)} partes | {n_temas} temas | {n_items} elementos")
    if faltan:
        print(f"Sin imagenes completas ({len(faltan)}): " + ", ".join(faltan))


if __name__ == "__main__":
    construir()
