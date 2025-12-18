### Nom de la faille
Exposition des fichiers sensibles
Cette faille implique la divulgation de fichiers sensibles tels que les fichiers de configuration ou les mots de passe hachés dans des fichiers accessibles publiquement, ce qui peut permettre à un attaquant d'obtenir des informations critiques pour accéder à des systèmes protégés.

## Contexte spécifique 
Dans ce cas, nous decouvrons via le fichier http://x.x.x.x/robots.txt l'existence d'une URL http://x.x.x.x/whatever, fichier contenant des informations sensibles, notamment un fichier .htpasswd, accessible publiquement. Ce fichier contient un mot de passe haché qui, une fois décrypté, donne l'accès à un info sensible. Ici, l'accès direct au fichier htpasswd révèle un mot de passe haché en MD5.


## Risques 
La divulgation de ce fichier sensible permet à un attaquant de récupérer un mot de passe haché qui peut être décrypté (MD5) pour accéder à des systèmes ou services protégés. Cela peut permettre un accès non autorisé à des informations confidentielles ou des ressources critiques. Ici par exemple il s'agit du mdp administrateur.


## Comment la trouver 
En accédant au chemin whatever, il est possible de découvrir une référence au fichier sensible .htpasswd. Ce fichier contient un mot de passe haché en MD5 + le nom admin "root". En décryptant le hash via un outil de décryptage MD5, on obtient le mot de passe en clair "qwerty123@". Nous pouvons alors acceder au compte admin via http://x.x.x.x/admin/ en entrant ce mdp et le nom root en tant que login.


## Ressources:
https://www.md5decrypt.org/ (outil de décryptage MD5)
Console du navigateur (DevTools > Network > Robots.txt)

## Flag: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

## Comment l'éviter 

- Protéger les fichiers sensibles comme .htpasswd en les plaçant dans des répertoires non accessibles publiquement.
- Utiliser un fichier .htaccess pour restreindre l'accès à ce type de fichiers et les empêcher d'être exposés via HTTP.
- Ajouter des règles spécifiques dans robots.txt pour interdire l'accès à certains fichiers sensibles aux moteurs de recherche, mais cela ne remplace pas une protection d'accès sur le serveur.
- Utiliser des méthodes de hachage modernes et robustes (par exemple, bcrypt) pour les mots de passe et ne pas exposer les hachages en texte clair.


## RESUME

http://192.168.56.3/robots.txt
http://192.168.56.3/whatever/
htpasswd
root:437394baff5aa33daa618be47b75cb49 (= login:password)
md5 decrypt: qwerty123@

