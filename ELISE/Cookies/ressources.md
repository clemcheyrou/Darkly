Nom de la faille/Definition
FR: Interception de cookies non securises
Cette faille implique la manipulation ou l’interception de cookies de session non protégés, permettant à un attaquant de se faire passer pour un utilisateur légitime.
EN: Cookie Poisoning / Insecure Cookie Interception
This vulnerability involves the manipulation or interception of unprotected session cookies, allowing an attacker to impersonate a legitimate user.

Contexte spécifique / Overview
FR: Dans le cas present, le site ne possede pas de certificat de securite HTTPS, et n'utilise donc pas de gestion de session securisee ou de cryptage des cookies via protocole SSl/TLS.
Si les cookies ne sont pas protégés, un attaquant peut les intercepter ou les modifier, et ainsi acceder au compte de la victime.
Un cookie nommé "I_am_admin" permettait de simuler un statut administrateur via une simple valeur MD5.
EN: In our case, the application was vulnerable because it was missing appropriate security hardening in the cookies session and weak http configuration (no cookie encryption by SSL/TLS protocols)
If the app isn't secured correctly, the attacker could intercept and modify it, and therefore access to the victim's account.
A cookie named "I_am_admin" allowed simulating admin status through a simple MD5 value change.

Risques / Risks
FR: En modifiant les donnees contenues initialement dans le cookie de session, un attaquant malveillant pourrait acceder au compte d'une victime via l'ID de cette session active (ID donne par le serveur a la connexion), sans avoir besoin de son identifiant ou de son mot de passe.
EN: An attacker could log in as admin without a password, potentially accessing sensitive data or critical functions.

Comment la trouver / How it was discovered
FR: Ici quand on ouvre la console dans l'onglet "Storage" puis "Cookies", on trouve un cookie de session nomme "I_am_admin". On se doute alors qu'il s'agit d'un petit indice subtil... Et l'on constate que la "value" associee a celui-ci est accessible et modifiable.
On recupere donc la valeur donnee:
I_am_admin:"b326b5062b2f0e69046810717534cb09"
Quand on decrypte cette donnee via une fonction de hashing md5, on constate qu'il s'agit de la traduction de "false".
On decide de traduire "true" pour faire un test, et on obtient :
b326b5062b2f0e69046810717534cb09
Quand on modifie le cookie avec cette valeur ... Surprise ! On obtient bien le flag :
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
EN:Cookie inspection via the browser "Storage" tab → modified "I_am_admin" cookie value after identifying a MD5 hash corresponding to "false". Then we translate and hash "true" via the md5 hash function.
And here is the flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

Ressources/Outils:
https://www.dcode.fr/md5-hash (hashing and decrypt md5)
Console du navigateur (DevTools > Storage > Cookies)

    68934a3e9455fa72420237eb05902327 = false
    b326b5062b2f0e69046810717534cb09 = true

Flag :                                       1      1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0

Comment l'eviter / How to fix it
FR:
- Utiliser HTTPS pour chiffrer les échanges.
- Définir les cookies avec les options sécurisées :
    HttpOnly : Empêche l’accès aux cookies par JavaScript.
    Secure : Empêche l’envoi du cookie en HTTP (uniquement HTTPS).
    SameSite=Strict : Empêche l’envoi des cookies sur des requêtes intersites.
- Regénérer l’identifiant de session après connexion pour éviter la fixation de session.
- Limiter la durée de vie des sessions pour réduire les risques d’attaques.
EN:
- Enforce HTTPS across the application
- Set cookies with :
    HttpOnly : This flag prevents JavaScript from accessing or modifying cookies. By setting this flag to true, the browser ensures that JavaScript on the client-side cannot manipulate cookies, protecting against XSS attacks.
    Secure : The Secure flag ensures that cookies are only transmitted over secure (HTTPS) connections. This helps prevent man-in-the-middle attacks, where attackers could intercept cookies if sent over an insecure connection (HTTP). This flag should always be set to true on websites using HTTPS
    SameSite=Strict : avoid sending cookies on intersites requests
- Regenerate sessions upon login
- Shorten session lifetime



