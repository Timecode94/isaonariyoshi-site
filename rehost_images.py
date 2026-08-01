#!/usr/bin/env python3
"""
Rapatrie les images du site depuis static.wixstatic.com vers un dossier local images/,
puis met à jour tous les fichiers .html pour qu'ils pointent vers les fichiers locaux.

Usage :
    python3 rehost_images.py

Aucune dépendance à installer (uniquement la bibliothèque standard Python).
À exécuter depuis le dossier qui contient les fichiers .html du site (celui où
se trouve aussi ce script).
"""

import glob
import os
import re
import urllib.request
import urllib.error

IMG_DIR = "images"
URL_PATTERN = re.compile(r'https://static\.wixstatic\.com/media/([^"]+)')

def main():
    html_files = glob.glob("*.html")
    if not html_files:
        print("Aucun fichier .html trouvé dans ce dossier. Lancez le script depuis le dossier du site.")
        return

    os.makedirs(IMG_DIR, exist_ok=True)pip3 install pillow

    # 1. Collecter toutes les URLs d'images uniques dans tous les fichiers HTML
    urls = set()
    for path in html_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        urls.update(URL_PATTERN.findall(content))

    print(f"{len(urls)} image(s) unique(s) trouvée(s) dans {len(html_files)} fichier(s) HTML.\n")

    # 2. Télécharger chaque image dans images/
    url_to_local = {}
    ok, failed = 0, []
    for i, path_part in enumerate(sorted(urls), 1):
        full_url = f"https://static.wixstatic.com/media/{path_part}"
        filename = path_part.split("/")[0]  # ex: 222d2c_xxxx~mv2.jpg (avant tout /v1/fill/...)
        local_path = os.path.join(IMG_DIR, filename)
        print(f"[{i}/{len(urls)}] {filename} ...", end=" ")
        try:
            req = urllib.request.Request(full_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=20) as response, open(local_path, "wb") as out:
                out.write(response.read())
            url_to_local[full_url] = f"{IMG_DIR}/{filename}"
            print("OK")
            ok += 1
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            print(f"ÉCHEC ({e})")
            failed.append(full_url)

    # 3. Remplacer les URLs dans tous les fichiers HTML
    for path in html_files:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        original = content
        for full_url, local_path in url_to_local.items():
            content = content.replace(full_url, local_path)
        if content != original:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Mis à jour : {path}")

    print(f"\nTerminé : {ok} image(s) téléchargée(s) dans {IMG_DIR}/, {len(failed)} échec(s).")
    if failed:
        print("URLs en échec (à retélécharger manuellement) :")
        for u in failed:
            print(f"  - {u}")

if __name__ == "__main__":
    main()
