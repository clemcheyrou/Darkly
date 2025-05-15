### Nom de la faille / Définition
Login Brute Force
Cette faille permet à un attaquant de deviner un mot de passe en testant automatiquement un grand nombre de combinaisons jusqu’à trouver les bons identifiants.

## Contexte spécifique / Overview
Le site possède une page de connexion située à l’URL index.php?page=signin. Aucun mécanisme de protection contre les attaques par force brute n’est en place (ex : limitation de tentatives, captcha, blocage IP etc).
En testant le nom d’utilisateur admin avec un simple script (ou mieux, avec l'outil Hydra), un mot de passe faible a été trouvé : shadow.

## Risques / Risks
Un attaquant peut accéder à un compte administrateur sans aucune vulnérabilité technique, simplement par force brute, si le mot de passe est faible et aucune protection n’est mise en place. Cela permet de compromettre tout le système.

## Comment la trouver / How it was discovered
On lance un script bash qui teste une quinzaine de mots de passe les plus courants, et on obtient le mdp shadow.
On se connecte ensuite avec "admin" et ce mdp. On obtient le flag.
ALTERNATIVE:
Via l’outil Hydra, en ciblant la page index.php?page=signin.
Commande utilisée :
 ` hydra -l admin -P ~/Downloads/10-million-password-list-top-100.txt -F -o hydra.log localhost:8080 http-get-form '/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif' `

	-l : nom d’utilisateur ciblé (admin)

	-P : dictionnaire de mots de passe courants

	-F : arrêt à la première tentative réussie

	-o : log de la tentative (hydra.log)

	http-get-form : méthode d’attaque sur formulaire GET

Le mot de passe trouvé : shadow


## Ressources / Outils
- script testant une quinzaine de mdp courants les uns apres les autres de facon automatisee (voir le script.sh)
ALTERNATIVE:
- Hydra – outil de brute force réseau
- puis donner en parametre a hydra une wordlist : 10-million-password-list-top-500.txt

## Flag
b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2

## Comment l’éviter / How to fix it
FR :
- Imposer des mots de passe robustes (longueur, complexité)
- Limiter les tentatives de connexion (ex : 5 essais max)
- Mettre en place un délai entre chaque tentative (progressif)
- Bloquer l’adresse IP temporairement après un certain nombre d’échecs
- Utiliser CAPTCHA après plusieurs échecs
- Logger toutes les tentatives échouées et les surveiller
