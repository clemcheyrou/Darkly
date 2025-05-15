### Nom de la faille/Definition
FR: Exposition des fichiers sensibles
Cette faille implique la divulgation de fichiers sensibles tels que les fichiers de configuration ou les mots de passe hachés dans des fichiers accessibles publiquement, ce qui peut permettre à un attaquant d'obtenir des informations critiques pour accéder à des systèmes protégés.

EN: Sensitive File Exposure
This vulnerability involves the exposure of sensitive files, such as configuration files or password hashes, that are publicly accessible, allowing an attacker to gain critical information that could be used to access protected systems.

## Contexte spécifique / Overview
FR: Dans ce cas, nous decouvrons via le fichier http://x.x.x.x/robots.txt l'existence d'une URL http://x.x.x.x/whatever, fichier contenant des informations sensibles, notamment un fichier .htpasswd, accessible publiquement. Ce fichier contient un mot de passe haché qui, une fois décrypté, donne l'accès à un info sensible. Ici, l'accès direct au fichier htpasswd révèle un mot de passe haché en MD5.

EN: In this case, a file containing sensitive information, including a .htpasswd file, is publicly accessible via the URL http://x.x.x.x/robots.txt. This file contains a hashed password that, once decrypted, provides access to a sensitive system. Direct access to the .htpasswd file also reveals an MD5 hashed password.

## Risques / Risks
FR: La divulgation de ce fichier sensible permet à un attaquant de récupérer un mot de passe haché qui peut être décrypté (MD5) pour accéder à des systèmes ou services protégés. Cela peut permettre un accès non autorisé à des informations confidentielles ou des ressources critiques. Ici par exemple il s'agit du mdp administrateur.

EN: Exposing this sensitive file allows an attacker to retrieve a hashed password that can be decrypted (MD5) to gain unauthorized access to protected systems or services. This could lead to unauthorized access to confidential information or critical resources.

## Comment la trouver / How it was discovered
FR: En accédant au chemin whatever, il est possible de découvrir une référence au fichier sensible .htpasswd. Ce fichier contient un mot de passe haché en MD5 + le nom admin "root". En décryptant le hash via un outil de décryptage MD5, on obtient le mot de passe en clair "qwerty123@". Nous pouvons alors acceder au compte admin via http://x.x.x.x/admin/ en entrant ce mdp et le nom root en tant que login.

EN: By accessing the robots.txt file, a reference to a sensitive file like .htpasswd was found. This file contains an MD5 hashed password. Decrypting this hash with an MD5 decryption tool reveals the plaintext password "qwerty123@."

## Ressources/Outils:
https://www.md5decrypt.org/ (outil de décryptage MD5)
Console du navigateur (DevTools > Network > Robots.txt)

## Flag: d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

## Comment l'éviter / How to fix it
FR:
- Protéger les fichiers sensibles comme .htpasswd en les plaçant dans des répertoires non accessibles publiquement.
- Utiliser un fichier .htaccess pour restreindre l'accès à ce type de fichiers et les empêcher d'être exposés via HTTP.
- Ajouter des règles spécifiques dans robots.txt pour interdire l'accès à certains fichiers sensibles aux moteurs de recherche, mais cela ne remplace pas une protection d'accès sur le serveur.
- Utiliser des méthodes de hachage modernes et robustes (par exemple, bcrypt) pour les mots de passe et ne pas exposer les hachages en texte clair.

EN:
- Protect sensitive files like .htpasswd by placing them in non-public directories.
- Use a .htaccess file to restrict access to such files and prevent them from being exposed via HTTP.
- Add specific rules in robots.txt to block search engines from accessing certain sensitive files, but this should not replace server-side access control
- Use modern and robust hashing methods (e.g., bcrypt) for passwords and avoid exposing hashes in plain text.




http://192.168.56.3/robots.txt
http://192.168.56.3/whatever/
htpasswd
root:437394baff5aa33daa618be47b75cb49 (= login:password)
md5 decrypt: qwerty123@

The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

Comment l'éviter:
Proteger htpasswd par un htaccess pour ne pas voir cette route (disallow pour le fichier robot ne suffit pas)
