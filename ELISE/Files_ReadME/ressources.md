Nom de la faille / Definition
FR : Fichiers sensibles révélés par robots.txt
Le fichier robots.txt, destiné à indiquer aux moteurs de recherche les pages à ne pas indexer, peut devenir un vecteur d’exposition de fichiers sensibles s’il contient des chemins confidentiels ou critiques.

EN : Sensitive Files Disclosure via robots.txt
The robots.txt file is meant to guide search engines on what not to index, but if it contains sensitive paths, it may inadvertently reveal critical resources to attackers.

Contexte spécifique / Overview
FR :
Dans ce cas, le fichier robots.txt révèle un répertoire caché nommé /.hidden. En visitant cette URL, on découvre une arborescence très profonde contenant des fichiers README à chaque niveau, dont la majorité sont des faux positifs ou des leurres.
Nous avons utilisé Scrapy, un module Python, pour automatiser l’exploration de ces répertoires et l’extraction des contenus pertinents. Un script a permis d’analyser tous les README récupérés et d’identifier un fichier contenant une chaîne ressemblant à un flag.

EN :
In this case, the robots.txt file discloses a hidden directory /.hidden. Visiting this URL reveals a deeply nested structure with numerous README files, most of them being decoys.
We used Scrapy, a Python scraping tool, to automate navigation and content extraction. A custom script was used to collect and analyze the content of all README files, successfully identifying a flag-like string.

Risques / Risks
FR :
- Révélation de chemins internes ou confidentiels à des utilisateurs non autorisés
- Automatisation possible de l'exploration et de l'extraction de fichiers.
- Risque d'exposition de données sensibles, d'informations système ou de flags dans un contexte CTF.

EN :
- Disclosure of internal or confidential paths to unauthorized users.
- Risk of automated file scraping and content extraction.
- Exposure of sensitive data or CTF flags through accessible but hidden files.


Comment la trouver / How it was discovered
FR :
- Nous avons commencé par scanner les chemins du serveur à l’aide de l’outil Dirb, découvrant le fichier /.hidden référencé dans robots.txt.
- En explorant les sous-dossiers, on a constaté la présence de nombreux fichiers README.
- Un scraper Scrapy a été configuré pour explorer chaque répertoire et récupérer les contenus uniques des README, stockés dans un dictionnaire en fonction de leur hash MD5.
- Le script a permis d’identifier un README contenant un flag :
"565245faf0b3998ad6fd6429f2ef67bd": ["http://x.x.x.x/.hidden/.../README", "99dde1d35d1fdd283924d84e6d9f1d820"]

EN :
- We started by scanning server paths using Dirb, and discovered the /.hidden path listed in robots.txt.
- Inside were deeply nested folders containing README files.
- A Scrapy spider was configured to recursively crawl and extract content from these files, filtering duplicates via MD5 hash.
- One README contained the flag:
"565245faf0b3998ad6fd6429f2ef67bd": ["http://x.x.x.x/.hidden/.../README", "99dde1d35d1fdd283924d84e6d9f1d820"]

Ressources/ Outils
- Dirb — Outil de brute-force de chemins web
- Scrapy — Framework Python de web scraping
- Navigateur web / Terminal
- Fichier robots.txt

Flag
99dde1d35d1fdd283924d84e6d9f1d820

Comment l’éviter / How to fix it
FR :
- Ne jamais inclure des chemins sensibles dans le fichier robots.txt. Celui-ci est publiquement accessible à l'adresse /robots.txt.
- Préférer les contrôles d’accès serveur (authentification, autorisations) pour protéger les ressources critiques.
- Mettre en place un mécanisme d'obfuscation ou mieux, ne pas exposer ces fichiers sur le serveur de production.
- Surveiller les accès à des répertoires inhabituels via les logs du serveur.

EN :
- Never include sensitive or hidden directories in robots.txt, as it is publicly accessible.
- Use proper access controls (authentication, authorization) to protect sensitive directories.
- Avoid deploying decoy or flag files in production or hide them using server-side mechanisms.
- Monitor access logs for unusual access to nested or hidden directories.
