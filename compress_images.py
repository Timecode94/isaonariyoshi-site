#!/usr/bin/env python3
"""
Redimensionne et compresse les images du dossier images/ pour un usage web
(elles sont actuellement en pleine résolution source, jusqu'à 15-20 Mo pièce).

Usage :
    pip3 install pillow
    python3 compress_images.py

À exécuter depuis le dossier du site (celui qui contient le dossier images/).
Les images sont écrasées sur place (redimensionnées à 1600px de large maximum,
converties en JPEG qualité 82 pour les .jpg, PNG optimisé pour les .png).
"""

import glob
import os

try:
    from PIL import Image
except ImportError:
    print("Le module Pillow n'est pas installé. Lancez d'abord :")
    print("  pip3 install pillow")
    raise SystemExit(1)

IMG_DIR = "images"
MAX_WIDTH = 1600

def main():
    if not os.path.isdir(IMG_DIR):
        print(f"Dossier '{IMG_DIR}/' introuvable. Lancez ce script depuis le dossier du site.")
        return

    files = glob.glob(os.path.join(IMG_DIR, "*"))
    total_before = sum(os.path.getsize(f) for f in files)

    for path in files:
        try:
            img = Image.open(path)
            fmt = img.format  # JPEG, PNG, etc.

            if img.width > MAX_WIDTH:
                ratio = MAX_WIDTH / img.width
                new_size = (MAX_WIDTH, int(img.height * ratio))
                img = img.resize(new_size, Image.LANCZOS)

            if fmt == "JPEG":
                img = img.convert("RGB")
                img.save(path, "JPEG", quality=82, optimize=True)
            elif fmt == "PNG":
                img.save(path, "PNG", optimize=True)
            else:
                img.save(path)

            print(f"{os.path.basename(path)} ... OK")
        except Exception as e:
            print(f"{os.path.basename(path)} ... ÉCHEC ({e})")

    total_after = sum(os.path.getsize(f) for f in glob.glob(os.path.join(IMG_DIR, "*")))
    print(f"\nAvant : {total_before / 1_000_000:.1f} Mo   →   Après : {total_after / 1_000_000:.1f} Mo")

if __name__ == "__main__":
    main()
