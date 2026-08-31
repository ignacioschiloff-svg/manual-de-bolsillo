"""Renombra el segundo lote de imagenes (WhatsApp) a los slugs ya escritos."""
import shutil
import sys
from pathlib import Path

IMGS = Path(__file__).parent / "imagenes"

PARES = [
    ("WhatsApp Image 2026-08-25 at 7.04.16 PM (3).jpeg", "WhatsApp Image 2026-08-25 at 7.04.16 PM (2).jpeg", "antagonistas-muscarinicos"),
    ("WhatsApp Image 2026-08-25 at 7.04.16 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.04.16 PM.jpeg", "antiemeticos"),
    ("WhatsApp Image 2026-08-25 at 7.04.56 PM (2).jpeg", "WhatsApp Image 2026-08-25 at 7.04.56 PM (1).jpeg", "polipos-colorrectales-cancer"),
    ("WhatsApp Image 2026-08-25 at 7.06.57 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.06.57 PM (2).jpeg", "crohn-colitis-ulcerosa"),
    ("WhatsApp Image 2026-08-25 at 7.06.57 PM (3).jpeg", "WhatsApp Image 2026-08-25 at 7.06.57 PM.jpeg", "gastritis-peptica"),
    ("WhatsApp Image 2026-08-25 at 7.11.08 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.11.08 PM.jpeg", "aminopenicilinas-penicilinas-espectro-extendido"),
    ("WhatsApp Image 2026-08-25 at 7.14.51 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.14.51 PM.jpeg", "higado-graso-alcoholico-no-alcoholico"),
    ("WhatsApp Image 2026-08-25 at 7.16.50 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.16.50 PM.jpeg", "nervios-craneales-i-ii"),
    ("WhatsApp Image 2026-08-25 at 7.17.51 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.17.51 PM.jpeg", "trastornos-gi-congenitos"),
    ("WhatsApp Image 2026-08-25 at 7.23.07 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.23.07 PM.jpeg", "enfermedad-cjd-parkinson-huntington"),
    ("WhatsApp Image 2026-08-25 at 7.23.56 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.23.56 PM.jpeg", "enfermedad-celiaca-malabsorcion"),
    ("WhatsApp Image 2026-08-25 at 7.25.12 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 7.25.12 PM.jpeg", "defectos-coagulacion-adquiridos"),
    ("WhatsApp Image 2026-08-25 at 8.05.32 PM (1).jpeg", "WhatsApp Image 2026-08-25 at 8.05.32 PM.jpeg", "trastornos-combinados-celulas-b-t"),
]


def main():
    ejecutar = "--si" in sys.argv
    for mapa, texto, slug in PARES:
        for archivo, sufijo in ((mapa, "mapa"), (texto, "texto")):
            origen = IMGS / archivo
            if not origen.is_file():
                print(f"[FALTA] {archivo}")
                continue
            destino = IMGS / f"{slug}-{sufijo}{origen.suffix}"
            print(f"{'[OK]' if ejecutar else '[prueba]'} {archivo} -> {destino.name}")
            if ejecutar:
                shutil.move(str(origen), str(destino))
    if not ejecutar:
        print("\n(prueba) ejecuta con --si para renombrar de verdad")


if __name__ == "__main__":
    main()
