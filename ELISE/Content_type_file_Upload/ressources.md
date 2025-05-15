### Nom de la faille / Définition
FR : Bypass de filtre de type MIME lors de l’upload de fichiers / MIME type Spoofing
Cette faille permet à un attaquant de contourner les protections basées sur le type MIME indiqué dans les en-têtes HTTP, en téléversant un fichier dangereux (ex: .php) déguisé avec un type de contenu inoffensif (ex: image/jpeg).

EN: MIME Type Filter Bypass on File Upload
This vulnerability allows an attacker to bypass file upload filters that rely solely on the MIME type in the HTTP headers by uploading a malicious file (e.g., .php) disguised as a safe type like image/jpeg.

## Contexte spécifique / Overview
FR :
Le site propose une page d’upload de fichiers accessible via /index.php?page=upload, permettant uniquement l’envoi de fichiers .jpeg. Lorsqu’on tente d’uploader un fichier .php, le serveur le rejette normalement en se basant sur l’en-tête Content-Type.
Cependant, en interceptant la requête HTTP et en modifiant manuellement le Content-Type en image/jpeg, le serveur accepte et stocke le fichier .php. Cela révèle que le système ne vérifie pas réellement le contenu du fichier, mais uniquement l’en-tête déclaré.

EN:
The application exposes a file upload page at /index.php?page=upload, which is supposed to accept only .jpeg files. When trying to upload a .php file, the server rejects it based on the Content-Type.
But by intercepting the request and manually changing the Content-Type to image/jpeg, the upload is accepted. This demonstrates the server trusts user-declared MIME types without further validation.

## Risques / Risks
FR :
- Exécution de code malveillant sur le serveur si le fichier .php est accepté par le backend.
- Prise de contrôle complète du serveur ou fuite de données sensibles.
- Accès à des fonctions critiques sans authentification.

EN:
- Arbitrary code execution if the .php file is interpreted.
- Full server compromise or sensitive data exposure.
- Unauthorized access to critical functions.

## Comment la trouver / How it was discovered
FR :
En accédant à la page d’upload /index.php?page=upload, on peut y envoyer des fichiers .jpeg.
Une tentative d’upload de fichier .php échoue :
Content-Type: application/octet-stream
Mais grace a une extension comme modheader, on peut modifier l’en-tête de Content-Type .
Le fichier est alors accepté et exécuté. Le flag est révélé :
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8

EN:
By visiting /index.php?page=upload, .jpeg files can be uploaded.
Trying to upload a .php file with its default MIME (application/octet-stream) fails.
But using Burp Suite to intercept and change Content-Type to image/jpeg — or via curl:
echo '<?php echo "I am bad" ?>' > /tmp/bad.php
curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/bad.php;type=image/jpeg" "http://x.x.x.x/index.php?page=upload"
The server accepts the file and executes it, revealing the flag:
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8

## Ressources / Outils :

- modheader extension
- Navigateur web + DevTools (pour vérifier l’envoi des headers)

## Comment l’éviter / How to fix it
FR :
- Ne jamais se baser uniquement sur le Content-Type envoyé par l’utilisateur.
- Appliquer une liste blanche d’extensions autorisées.
- Renommer le fichier à l’upload pour éviter qu’il soit exécutable.
- Analyser le contenu réel du fichier (magic bytes) pour vérifier sa nature.
- Limiter les répertoires accessibles en écriture/exécution.
- Vérifier la taille du fichier.
- Empêcher l'exécution de fichiers dans les dossiers d’upload (désactiver l’exécution PHP).
- Forcer les permissions (chmod) sur les fichiers uploadés.
- htaccess

EN:
- Never trust Content-Type headers from user input.
- Apply a whitelist of allowed file extensions.
- Rename uploaded files to prevent execution.
- Inspect file content (e.g., magic bytes) to verify type.
- Restrict write/execute permissions to upload directories.
- Check file size limits.
- Disable PHP execution in upload folders.
- Set safe file permissions upon upload.

## Flag :
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
