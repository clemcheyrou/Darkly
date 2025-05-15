# Nom de la faille
DOM-based XSS et Formulaire Non Protégé

## Définition
Le DOM-based XSS (Cross-Site Scripting) est une vulnérabilité de sécurité qui permet à un attaquant d'injecter du code JavaScript malveillant dans le DOM (Document Object Model) d'une page web. Contrairement aux autres types de XSS, le DOM-based XSS se produit lorsque le code malveillant est exécuté dans le contexte du navigateur de la victime, sans que le serveur ne soit directement impliqué.

Un formulaire non protégé est une vulnérabilité où les entrées utilisateur ne sont pas correctement validées ou échappées, permettant des attaques telles que l'injection de code malveillant.

## Risques
Les attaques DOM-based XSS et les formulaires non protégés présentent plusieurs risques majeurs pour la sécurité des applications web :

- **Vol de données sensibles**
- **Manipulation du contenu de la page**
- **Redirection vers des sites malveillants**
- **Exécution de commandes arbitraires**

## Détection et Exploitation

### Détection

1. **Vérification des formulaires non protégés** :
   - Identifiez les formulaires qui n'ont pas de validation ou d'échappement des entrées utilisateur.
   - Vérifiez si les valeurs des options de sélection sont protégées côté serveur.

### Exploitation

1. **Exploitation des formulaires non protégés** :
   - Modifiez les valeurs des options de sélection pour injecter du code malveillant ou accéder à des informations sensibles.
   - Par exemple, modifiez la valeur de l'option `<option value="2">2</option>` pour injecter du code malveillant.
   - Envoyez la valeur modifiée au backend pour exploiter la vulnérabilité.

2. **Obtention du flag** :
   - En exploitant la vulnérabilité DOM-based XSS et les formulaires non protégés, vous pouvez obtenir le flag suivant :
     - Flag : `03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa`

## Comment l'éviter

1. **Utiliser des frameworks sécurisés** :
   - Utilisez des frameworks qui offrent des protections intégrées contre les attaques XSS, comme React, Angular, ou Vue.js.

2. **Protéger les formulaires** :
   - Validez et échappez les entrées utilisateur dans les formulaires pour éviter les injections de code malveillant.
   - Vérifiez les valeurs des options de sélection côté serveur pour éviter les manipulations malveillantes.
   - Assurez-vous que les valeurs envoyées au backend sont correctement validées et échappées.

## Source
- [OWASP DOM-based XSS](https://owasp.org/www-community/Types_of_Cross-Site_Scripting#DOM_Based_XSS)
- [PortSwigger DOM-based XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based)
