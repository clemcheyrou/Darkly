# Nom de la faille
Injections HTML

## Définition

Les **injections de HTML** sont une forme de **Cross-Site Scripting (XSS)**. Elles permettent à un attaquant d'injecter du code HTML ou JavaScript malveillant dans une page web consultée par un utilisateur.

Même si cela ressemble à une simple modification de l'interface, cela peut être utilisé pour voler des données, rediriger l'utilisateur, ou exécuter du code non autorisé dans son navigateur.

## Détection et exploitation

Dans ce cas précis :

- L'**input utilisateur est limité** à une seule lettre parmi les suivantes :  
  `p, a, r, t, i, c, l, e, s`

Cela empêche les caractères spéciaux nécessaires à une XSS classique (`<`, `>`, `"`, `'`, etc.) d’être utilisés.

## Flag obtenu
0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e

## Comment l’éviter

1. **Échapper les caractères spéciaux HTML**

Pour prévenir ce type de vulnérabilité, il est essentiel d’**échapper les caractères spéciaux** dans tout contenu HTML généré dynamiquement à partir d'une entrée utilisateur.