68934a3e9455fa72420237eb05902327 = false
b326b5062b2f0e69046810717534cb09 = true

Aller sur la page login et changer le cookie:
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

Comme l'éviter:

Securing Cookies
HTTP Only Flag:

This flag prevents JavaScript from accessing or modifying cookies. By setting this flag to true, the browser ensures that JavaScript on the client-side cannot manipulate cookies, protecting against XSS attacks.

Secure Flag:

The Secure flag ensures that cookies are only transmitted over secure (HTTPS) connections. This helps prevent man-in-the-middle attacks, where attackers could intercept cookies if sent over an insecure connection (HTTP). This flag should always be set to true on websites using HTTPS.