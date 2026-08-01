# Site isaonariyoshi.com — version statique

Site statique (HTML/CSS pur, aucune dépendance à installer) reconstruit à partir du contenu du site Wix d'origine.

## 1. Tester en local (avant tout déploiement)

Ouvrez simplement `index.html` en double-cliquant dessus, ou faites glisser le dossier dans votre navigateur. Toutes les pages et images doivent s'afficher (les images restent hébergées sur les serveurs Wix pour l'instant — voir section 4).

## 2. Déployer sur GitHub Pages (gratuit)

1. Créez un compte sur [github.com](https://github.com) si vous n'en avez pas.
2. Créez un nouveau dépôt (bouton vert "New repository"), nommez-le par exemple `isaonariyoshi-site`, cochez "Public".
3. Sur la page du dépôt, cliquez sur "uploading an existing file" et glissez-déposez **tous les fichiers de ce dossier** (index.html, style.css, les autres .html — pas besoin d'uploader ce README).
4. Cliquez "Commit changes".
5. Allez dans **Settings → Pages** (menu de gauche).
6. Sous "Build and deployment", choisissez **Deploy from a branch**, branche `main`, dossier `/ (root)`. Sauvegardez.
7. Au bout d'1 à 2 minutes, GitHub vous donne une URL du type `https://votrenomdutilisateur.github.io/isaonariyoshi-site/` — c'est votre site en ligne.

## 3. Brancher votre nom de domaine isaonariyoshi.com

1. Toujours dans **Settings → Pages**, dans le champ "Custom domain", entrez `isaonariyoshi.com` et sauvegardez (GitHub crée automatiquement un fichier `CNAME` dans votre dépôt).
2. Chez votre registrar de domaine (là où vous gérez le DNS — Wix, OVH, Gandi...), ajoutez ces enregistrements DNS :
   - Un enregistrement **A** pointant vers chacune de ces IPs GitHub : `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - Un enregistrement **CNAME** pour `www` pointant vers `votrenomdutilisateur.github.io`
3. La propagation DNS prend entre quelques minutes et 24-48h.
4. Cochez "Enforce HTTPS" dans les paramètres Pages une fois le domaine reconnu, pour avoir un certificat SSL gratuit.

## 4. Important — les images sont encore hébergées chez Wix

Pour l'instant, les balises `<img>` pointent vers les serveurs `static.wixstatic.com`. Ça fonctionne tant que ces URLs restent actives, mais idéalement il faut les rapatrier :

1. Téléchargez chaque image (clic-droit → Enregistrer l'image sous) dans un dossier `images/` à la racine du site.
2. Remplacez dans chaque fichier `.html` les URLs `https://static.wixstatic.com/...` par `images/nom-du-fichier.jpg`.

Je peux vous aider à faire ce remplacement en masse si vous me confirmez que vous avez téléchargé les images.

## 5. Ce qui manque encore

- **Album Photo** : 4 photos sur 7 n'ont pas pu être récupérées automatiquement (carrousel). Voir la note sur cette page.
- **Formulaire de contact** : remplacé par un simple lien `mailto:` fonctionnel (un vrai formulaire nécessiterait un service tiers comme Formspree, gratuit jusqu'à un certain volume).
