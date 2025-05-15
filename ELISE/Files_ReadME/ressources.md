### Nom de la faille / Definition
Fichiers sensibles révélés par robots.txt
Le fichier robots.txt, destiné à indiquer aux moteurs de recherche les pages à ne pas indexer, peut devenir un vecteur d’exposition de fichiers sensibles s’il contient des chemins confidentiels ou critiques.

## Contexte spécifique / Overview
Dans ce cas, le fichier robots.txt révèle un répertoire caché nommé /.hidden. En visitant cette URL, on découvre une arborescence très profonde contenant des fichiers README à chaque niveau, dont la majorité sont des fausses pistes vides.
Nous avons utilisé Scrapy, un module Python, pour automatiser l’exploration de ces répertoires et l’extraction des contenus interessants. Notre script a permis d’analyser tous les README récupérés et d’identifier un fichier contenant une chaîne ressemblant à un flag.

## Risques / Risks
- Révélation de chemins internes ou confidentiels à des utilisateurs non autorisés
- Automatisation possible de l'exploration et de l'extraction de fichiers.
- Risque d'exposition de données sensibles, d'informations système (ou de flags comme ici dans un contexte CTF).


## Comment la trouver / How it was discovered
- Nous avons commencé par explorer tous les chemins en découvrant le fichier /.hidden référencé dans robots.txt.
- En explorant les sous-dossiers, on a constaté la présence de nombreux fichiers README.
- Un scraper Scrapy a été configuré pour explorer chaque répertoire et récupérer les contenus uniques des README, stockés dans un dictionnaire en fonction de leur hash MD5.
- Le script a permis d’identifier un README contenant un flag :
"565245faf0b3998ad6fd6429f2ef67bd": ["http://x.x.x.x/.hidden/.../README", "99dde1d35d1fdd283924d84e6d9f1d820"]

## Ressources/ Outils
- Scrapy — Framework Python de web scraping
- Navigateur web / Terminal
- Fichier robots.txt

## Flag
99dde1d35d1fdd283924d84e6d9f1d820

## Comment l’éviter / How to fix it
- Ne jamais inclure des chemins sensibles dans le fichier robots.txt car celui-ci est publiquement accessible à l'adresse /robots.txt.
- Préférer les contrôles d’accès serveur (authentification, autorisations) pour protéger les ressources critiques.
- Mettre en place un mécanisme d'obfuscation ou mieux, ne pas exposer ces fichiers sur le serveur de production.
- Surveiller les accès à des répertoires inhabituels via les logs du serveur.
