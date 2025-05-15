# Nom de la faille
DOM-based XSS

## Définition
Le DOM-based XSS (Cross-Site Scripting) est une vulnérabilité de sécurité qui permet à un attaquant d'injecter du code JavaScript malveillant dans le DOM (Document Object Model) d'une page web. Contrairement aux autres types de XSS, le DOM-based XSS se produit lorsque le code malveillant est exécuté dans le contexte du navigateur de la victime, sans que le serveur ne soit directement impliqué.

## Risques
Les attaques DOM-based XSS présentent plusieurs risques majeurs pour la sécurité des applications web :

- **Vol de données sensibles**
- **Manipulation du contenu de la page** : Les attaquants peuvent modifier le contenu de la page web pour tromper les utilisateurs ou les inciter à effectuer des actions non désirées.
- **Redirection vers des sites malveillants**
- **Exécution de commandes** 

## Détection et Exploitation

### Détection
1. **Manipulation du DOM** :
   - Utilisez les outils de développement du navigateur pour manipuler le DOM et observer les changements.
   - Par exemple, supprimez l'attribut `hidden` d'une balise HTML `input` pour voir si cela révèle des informations sensibles ou des champs de formulaire cachés.

### Exploitation

1. **Obtention du flag** :
   - En exploitant la vulnérabilité DOM-based XSS, vous pouvez obtenir le flag suivant :
     - Flag : `1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0`

## Comment l'éviter

1. **Ne pas utiliser l'attribut `hidden` pour masquer des informations sensibles** :
   - Évitez d'utiliser l'attribut `hidden` pour masquer des informations sensibles ou des champs de formulaire. Utilisez des méthodes de sécurité plus robustes pour protéger les données sensibles.

## Source
- [OWASP DOM-based XSS](https://owasp.org/www-community/Types_of_Cross-Site_Scripting#DOM_Based_XSS)
- [PortSwigger DOM-based XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based)
