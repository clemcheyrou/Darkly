### Nom de la faille / Définition
FR : Brute Force sur formulaire de connexion
Cette faille permet à un attaquant de deviner un mot de passe en testant automatiquement un grand nombre de combinaisons jusqu’à trouver les bons identifiants.
EN : Login Brute Force
This vulnerability allows an attacker to guess a password by automatically testing a large number of combinations until the correct credentials are found.

## Contexte spécifique / Overview
FR:
Le site possède une page de connexion située à l’URL index.php?page=signin. Aucun mécanisme de protection contre les attaques par force brute n’est en place (ex : limitation de tentatives, captcha, blocage IP).
En testant le nom d’utilisateur admin avec l’outil Hydra, un mot de passe faible a été trouvé : shadow.
EN :
The application has a login page at index.php?page=signin. It lacks brute force protection (such as attempt rate limiting, captcha, or IP blocking).
Using the username admin, we launched a Hydra brute force attack and successfully found the password shadow.

## Risques / Risks
FR :
Un attaquant peut accéder à un compte administrateur sans aucune vulnérabilité technique, simplement par force brute, si le mot de passe est faible et aucune protection n’est mise en place. Cela permet de compromettre tout le système.
EN :
An attacker can gain admin access just by brute-forcing a weak password if there are no countermeasures. This could compromise the whole system.

## Comment la trouver / How it was discovered
FR :
Via l’outil Hydra, en ciblant la page index.php?page=signin.
Commande utilisée :
 ` hydra -l admin -P ~/Downloads/10-million-password-list-top-100.txt -F -o hydra.log localhost:8080 http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif' `

	-l : nom d’utilisateur ciblé (admin)

	-P : dictionnaire de mots de passe courants

	-F : arrêt à la première tentative réussie

	-o : log de la tentative (hydra.log)

	http-get-form : méthode d’attaque sur formulaire GET
Le mot de passe trouvé : shadow

EN :
We used Hydra on the login form. The command:
hydra -l admin -P /root/dictionary/10-million-password-list-top-500.txt -F -o hydra.log x.x.x.x http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif'
This discovered that the correct password for admin was shadow.

## Ressources / Outils
- Hydra – outil de brute force réseau
- Wordlist : 10-million-password-list-top-500.txt (fournie dans Dockerfile)
- DevTools : inspection du formulaire pour comprendre les paramètres GET
- Exemple d'URL brute-forcée :
/index.php?page=signin&username=admin&password=shadow&Login=Login

## Flag
B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2

## Comment l’éviter / How to fix it
FR :
- Imposer des mots de passe robustes (longueur, complexité)
- Limiter les tentatives de connexion (ex : 5 essais max)
- Mettre en place un délai entre chaque tentative (progressif)
- Bloquer l’adresse IP temporairement après un certain nombre d’échecs
- Utiliser CAPTCHA après plusieurs échecs
- Logger toutes les tentatives échouées et les surveiller
EN :
- Enforce strong password policies
- Limit login attempts (e.g., 5 tries max)
- Add delay between attempts
- Ban IP addresses after repeated failures
- Use a CAPTCHA mechanism
- Log and monitor failed login attempts
