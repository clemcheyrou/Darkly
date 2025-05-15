### Nom de la faille / Definition
Falsification de requêtes côté serveur (SSRF)
Cette faille permet à un attaquant d’abuser d’un serveur vulnérable pour envoyer des requêtes non autorisées vers des ressources internes ou externes, contournant potentiellement des contrôles d’accès, exfiltrant des données ou réalisant d'autres attaques.

## Contexte spécifique / Overview
Dans ce cas, le site accepte des entrées utilisateur non filtrées dans les en-têtes HTTP comme Referer ou User-Agent. Grâce à l’extension ModHeader, on peut manipuler ces en-têtes pour tromper le serveur en effectuant des requêtes vers des ressources internes ou non prévues. Cela permet par exemple d’accéder à des services internes, de contourner des contrôles d'accès ou d’injecter des scripts.

## Risques / Risks
- Contournement de contrôle d'accès
- Accès à des ressources internes normalement inaccessibles
- Lancement d'attaques en chaîne (scan de ports internes, attaque SSRF vers metadata services, etc.)
- Injection de code (XSS via User-Agent ou Referer manipulés)

## Comment la trouver / How it was discovered

- En utilisant l’extension ModHeader dans le navigateur, on ajoute ou modifie les en-têtes Referer et User-Agent.
- Exemple d’en-tête Referer malveillant : https://www.nsa.gov/
- Exemple de User-Agent injectant du code : ft_bornToSec
- En modifiant ces valeurs, on observe que le serveur ne les filtre pas et agit en fonction de ces entrées. Cela a permis d’obtenir un comportement non prévu menant à la découverte du flag.
Flag obtenu :
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

## Ressources / Outils
- ModHeader – Extension Chrome/Firefox pour manipuler les en-têtes HTTP
- Navigateur Web (pour observer les réponses et comportements)
- Documentation OWASP SSRF : https://portswigger.net/web-security/ssrf
- XSS Filter Evasion Cheat Sheet

## The flag is :
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

## Comment l'eviter:
- Verifier les entrees des en-tetes
- X-Content-Type-Options(indiquer que les types MIME annoncés dans les en-têtes Content-Type ne doivent pas être modifiés ou et suivis)

## Comment l’éviter / How to fix it
FR :
- Ne jamais faire confiance aux en-têtes comme Referer, User-Agent, etc.
- Valider et filtrer strictement toutes les entrées utilisateur, y compris dans les en-têtes.
- Implémenter une liste blanche stricte des destinations autorisées en cas de redirection ou de chargement externe.
- Utiliser l’en-tête X-Content-Type-Options: nosniff pour éviter l’interprétation incorrecte du type de contenu.
- Isoler les services internes via pare-feu et éviter les accès directs depuis le frontend.
