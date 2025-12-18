# Nom de la faille
Open redirect ou « redirection ouverte »

## Définition
Il s’agit d’une vulnérabilité qui peut avoir un impact important sur les utilisateurs d’une application web puisque son exploitation la plus classique permet de voler les identifiants des utilisateurs piégés.

## Risques
Dans la plupart des cas, les attaquants utilisent les vulnérabilités open redirect afin de dérober les identifiants des utilisateurs piégés.

Plus rarement, les attaquants peuvent également se servir des vulnérabilités open redirect pour faire effectuer à sa victime des actions sans leur consentement.

Et ici permet d'acceder a des pages non authorisees.

## Détection et exploitation

### Détection
Pour savoir si votre application web possède une vulnérabilité open redirect, il faut commencer par partir à la recherche des fonctionnalités de redirection qu’elle peut contenir :
- Les liens de redirection après une authentification
- Les liens de confirmation d'inscription
- Les pages de redirection après une action
- Les pages d'erreur personnalisées
- Les mécanismes de logout (déconnexion)

- **Les liens de redirection vers les reseaux comme ici**

Le test le plus simple est bien sûr de reperer un "redirect" dans l'url, puis de changer le nom de domaine a la suite du mot-cle "site" et de constater ou non une redirection. 

### Exploitation
Ici on renseigne 'admin' (ou autre chose) a la place de la redirection vers les RS comme Twitter par exemple

```
http://192.168.56.102/index.php?page=redirect&site=admin
```
Flag obtenu->
b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3

## Comment l'éviter
- Éviter les redirections
- Validation des URL
- Utiliser des URL relatives
- Whitelist de destinations
- Ajouter une couche d’abstraction
- Avertir l’utilisateur qu’il quitte votre application web

### Sources
https://www.it-connect.fr/securite-des-applications-web-vulnerabilite-open-redirect/
