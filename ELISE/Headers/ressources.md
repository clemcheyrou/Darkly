### Nom de la faille / Definition
FR : Falsification de requêtes côté serveur (SSRF)
Cette faille permet à un attaquant d’abuser d’un serveur vulnérable pour envoyer des requêtes non autorisées vers des ressources internes ou externes, contournant potentiellement des contrôles d’accès, exfiltrant des données ou réalisant d'autres attaques.
EN : Server-Side Request Forgery (SSRF)
This vulnerability allows an attacker to make a vulnerable server issue unauthorized requests to internal or external systems, potentially bypassing access controls, leaking data, or performing other malicious actions.

## Contexte spécifique / Overview
FR : Dans ce cas, le site accepte des entrées utilisateur non filtrées dans les en-têtes HTTP comme Referer ou User-Agent. Grâce à l’extension ModHeader, on peut manipuler ces en-têtes pour tromper le serveur en effectuant des requêtes vers des ressources internes ou non prévues. Cela permet par exemple d’accéder à des services internes, de contourner des contrôles d'accès ou d’injecter des scripts.
EN : In this scenario, the application accepts unvalidated user input in HTTP headers like Referer or User-Agent. Using ModHeader, these headers can be modified to trick the server into making requests to unintended or internal resources. This may allow internal service access, bypassing access controls or injecting malicious scripts.

## Risques / Risks
FR :
- Contournement de contrôle d'accès
- Accès à des ressources internes normalement inaccessibles
- Lancement d'attaques en chaîne (scan de ports internes, attaque SSRF vers metadata services, etc.)
- Injection de code (XSS via User-Agent ou Referer manipulés)

EN :
- Bypass access controls
-Unauthorized access to internal services
- Possibility of chained attacks (e.g., internal port scanning, SSRF to metadata services)
- Potential for code injection (XSS via forged User-Agent or Referer headers)

## Comment la trouver / How it was discovered
FR :
- En utilisant l’extension ModHeader dans le navigateur, on ajoute ou modifie les en-têtes Referer et User-Agent.
- Exemple d’en-tête Referer malveillant : http://127.0.0.1/admin
- Exemple de User-Agent injectant du code : <script>alert('XSS')</script>
- En modifiant ces valeurs, on observe que le serveur ne les filtre pas et agit en fonction de ces entrées. Cela a permis d’obtenir un comportement non prévu menant à la découverte du flag.
Flag obtenu :
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

EN :
- Using the ModHeader browser extension, we added or changed headers like Referer and User-Agent.
- Example malicious Referer: http://127.0.0.1/admin
- Example User-Agent injecting script: <script>alert('XSS')</script>
- The server did not sanitize or validate these headers, which led to unintended behavior and ultimately revealed the flag:
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

EN :
- Never trust headers like Referer, User-Agent, etc.
- Strictly validate and filter all user input, including HTTP headers.
- Implement strict allow-lists for external requests or redirects.
- Use X-Content-Type-Options: nosniff to prevent MIME-type sniffing.
- Isolate internal services via firewalls and block direct access from user-facing applications.








https://portswigger.net/web-security/ssrf

Utilise modHeader pour modifier les headers de la requete HTTP.

Referer: elle l'endroit dont on est 'arrive' (contourner controle d'acces, XSS, envoye des donnees)
User-Agent: envoye par le navigateur au serveur pour identifier le logiciel client qui effectue la requête (tromper le serveur, XSS, contourner protections)
