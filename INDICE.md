# 📚 Manual de Bolsillo — Índice general

Colección de análisis en formato Sketcheador (4 pasos por número).
Cada tema tiene su propio archivo. Este índice es el mapa de todo.

---

## Parte 1 — Bacterias Gram-positivas

| Tema | Archivo |
|---|---|
| Staphylococcus aureus | [ver](01-gram-positivas/staphylococcus-aureus.md) |
| Staphylococcus epidermidis & saprophyticus | [ver](01-gram-positivas/staphylococcus-epidermidis-saprophyticus.md) |
| Enterococcus faecium & faecalis | [ver](01-gram-positivas/enterococcus-faecium-faecalis.md) |
| Listeria monocytogenes | [ver](01-gram-positivas/listeria-monocytogenes.md) |
| Corynebacterium diphtheriae | [ver](01-gram-positivas/corynebacterium-diphtheriae.md) |
| Actinomyces israelii | [ver](01-gram-positivas/actinomyces-israelii.md) |
| Nocardia asteroides | [ver](01-gram-positivas/nocardia-asteroides.md) |
| Clostridium botulinum | [ver](01-gram-positivas/clostridium-botulinum.md) |
| Clostridium tetani | [ver](01-gram-positivas/clostridium-tetani.md) |
| Clostridium perfringens | [ver](01-gram-positivas/clostridium-perfringens.md) |
| Clostridioides difficile | [ver](01-gram-positivas/clostridioides-difficile.md) |

## Parte 2 — Bacterias Gram-negativas

| Tema | Archivo |
|---|---|
| Moraxella catarrhalis | [ver](02-gram-negativas/moraxella-catarrhalis.md) |
| Haemophilus influenzae | [ver](02-gram-negativas/haemophilus-influenzae.md) |
| Bordetella pertussis | [ver](02-gram-negativas/bordetella-pertussis.md) |
| Brucella spp. | [ver](02-gram-negativas/brucella.md) |
| Francisella tularensis | [ver](02-gram-negativas/francisella-tularensis.md) |
| Pasteurella multocida | [ver](02-gram-negativas/pasteurella-multocida.md) |
| Escherichia coli (ETEC & EHEC) | [ver](02-gram-negativas/escherichia-coli.md) |
| Klebsiella, Enterobacter, Serratia | [ver](02-gram-negativas/klebsiella-enterobacter-serratia.md) |
| Proteus mirabilis | [ver](02-gram-negativas/proteus-mirabilis.md) |
| Salmonella enteritidis & typhi | [ver](02-gram-negativas/salmonella.md) |
| Shigella spp. | [ver](02-gram-negativas/shigella.md) |
| Yersinia enterocolitica & pestis | [ver](02-gram-negativas/yersinia.md) |
| Vibrio spp. | [ver](02-gram-negativas/vibrio.md) |
| Campylobacter jejuni | [ver](02-gram-negativas/campylobacter-jejuni.md) |

## Parte 3 — Rickettsias

| Tema | Archivo |
|---|---|
| Rickettsia — Visión general | [ver](03-rickettsias/rickettsia-overview.md) |
| Rickettsia rickettsii | [ver](03-rickettsias/rickettsia-rickettsii.md) |
| Rickettsia prowazekii | [ver](03-rickettsias/rickettsia-prowazekii.md) |

## Parte 4 — Virus

| Tema | Archivo |
|---|---|
| Poliomavirus JC y BK (Polyomaviridae) | [ver](04-virus/poliomavirus-jc-bk.md) |
| Virus de la Rabia (Rhabdoviridae) | [ver](04-virus/rabia.md) |

## Parte 5 — Patología GI y hepática

| Tema | Archivo |
|---|---|
| Tumores hepáticos y carcinoma hepatocelular | [ver](05-patologia-gi/tumores-hepaticos-hcc.md) |
| Tumor carcinoide y neoplasias de intestino delgado | [ver](05-patologia-gi/carcinoide-intestino-delgado.md) |
| Pólipos colorrectales y cáncer | [ver](05-patologia-gi/polipos-colorrectales-cancer.md) |

## Parte 6 — Hematología

| Tema | Archivo |
|---|---|
| Policitemia | [ver](06-hematologia/policitemia.md) |

## Parte 7 — Farmacología

| Tema | Archivo |
|---|---|
| Antagonistas muscarínicos | [ver](07-farmacologia/antagonistas-muscarinicos.md) |
| Antieméticos | [ver](07-farmacologia/antiemeticos.md) |
| Anticuerpos monoclonales | [ver](07-farmacologia/anticuerpos-monoclonales.md) |
| Macrólidos | [ver](07-farmacologia/macrolidos.md) |
| Vancomicina | [ver](07-farmacologia/vancomicina.md) |
| Laxantes y antidiarreicos | [ver](07-farmacologia/laxantes-antidiarreicos.md) |

---

# 🖼️ Cómo poner las imágenes

Cada Sketchy usa **dos imágenes**: el dibujo con los números y la hoja de texto.

Guárdalas en la carpeta `imagenes` con este nombre exacto:

```
imagenes/nombre-del-tema-mapa.png     ← el dibujo con los números
imagenes/nombre-del-tema-texto.png    ← la hoja con las explicaciones
```

Ejemplo para Staph aureus:

```
imagenes/staphylococcus-aureus-mapa.png
imagenes/staphylococcus-aureus-texto.png
```

El nombre del tema es el mismo del archivo `.md`. Si respetas el nombre,
las imágenes aparecen solas al abrir el documento.

---

# ➕ Cómo añadir un Sketchy nuevo

1. Elige a qué Parte pertenece (Gram-positiva, Gram-negativa, virus, etc.).
2. Crea el archivo `.md` dentro de esa carpeta.
3. Agrega una fila a la tabla de esa Parte, aquí arriba.
4. Guarda las dos imágenes en `imagenes` con el nombre correspondiente.

Si el tema no encaja en ninguna Parte, se crea una nueva Parte al final
(Parte 8, Parte 9…) sin tocar la numeración de las anteriores.

---

# 🧩 Formato de cada ficha

```
🔢 [Número]. [Nombre del elemento en la imagen]

🎨 ¿Qué se ve en la imagen?
[objeto / personaje / símbolo]

💡 ¿Qué significa clínicamente?
[diagnóstico o hallazgo]

🧠 ¿Qué dice Sketchy y cómo interpretarlo?
[cómo lo presenta, qué mnemotecnia usa]

📜 Texto literal de Sketchy:
[texto exacto, sin traducir]
```
