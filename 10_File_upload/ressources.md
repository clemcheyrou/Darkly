### Nom de la faille 
MIME type Spoofing

Cette faille permet à un attaquant de contourner les protections basées sur le type MIME indiqué dans les en-têtes HTTP, en téléchargeant un fichier dangereux (ex: .php) déguisé avec un type de contenu inoffensif (ex: image/jpeg).

## Contexte spécifique 
Le site propose une page d’upload de fichiers accessible via /index.php?page=upload, permettant uniquement l’envoi de fichiers .jpeg. Lorsqu’on tente d’uploader un fichier .php, le serveur le rejette normalement en se basant sur l’en-tête Content-Type.
Cependant, en interceptant la requête HTTP et en modifiant manuellement le Content-Type en image/jpeg, le serveur accepte et stocke le fichier .php. Cela révèle que le système ne vérifie pas réellement le contenu du fichier, mais uniquement l’en-tête déclaré.

## Risques 
- Exécution de code malveillant sur le serveur si le fichier .php est accepté par le backend.
- Prise de contrôle complète du serveur ou fuite de données sensibles.
- Accès à des fonctions critiques sans authentification.

## Comment la trouver 
En accédant à la page d’upload /index.php?page=upload, on peut y envoyer des fichiers .jpeg.
Une tentative d’upload de fichier .php échoue pour cette raison:
"Content-Type: application/octet-stream"

Nous pouvons utiliser un simple script curl qui permet de forcer le telechargement d'un contenu php en le faisant passer pour une image/jpeg. Voici le script:
` echo '<?php echo "Am I here?" ?>' > /tmp/test.php `
puis :
` curl -X POST -F "Upload=Upload" -F "uploaded=@/tmp/test.php;type=image/jpeg" "http://192.168.56.103/index.php?page=upload#" | grep -i 'flag' `

Le fichier est alors accepté et exécuté.

Le flag est intercepte :
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8

## Ressources / Outils :
- modheader extension
- script curl pour forcer l'upload d'un content-type non attendu
- Navigateur web + DevTools (pour vérifier l’envoi des headers)

## Comment l’éviter 
- Ne jamais se baser uniquement sur le Content-Type envoyé par l’utilisateur.
- Appliquer une liste blanche d’extensions autorisées.
- Verifier le nom complet du fichier hors extensionrévélé
- Empêcher l'exécution de fichiers dans les dossiers d’upload (désactiver l’exécution PHP).

## Flag :
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
