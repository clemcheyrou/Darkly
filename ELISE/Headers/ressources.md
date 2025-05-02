https://portswigger.net/web-security/ssrf

Utilise modHeader pour modifier les headers de la requete HTTP.

Referer: elle l'endroit dont on est 'arrive' (contourner controle d'acces, XSS, envoye des donnees)
User-Agent: envoye par le navigateur au serveur pour identifier le logiciel client qui effectue la requête (tromper le serveur, XSS, contourner protections)

The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

Comment l'eviter:
- Verifier les entrees des en-tetes
- X-Content-Type-Options(indiquer que les types MIME annoncés dans les en-têtes Content-Type ne doivent pas être modifiés ou et suivis)
