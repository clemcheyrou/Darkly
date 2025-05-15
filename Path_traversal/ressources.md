## Nom de la faille
Path Traversal

### Définition

Le **path traversal** (ou traversal de chemin) est une vulnérabilité de sécurité permettant à un attaquant d'accéder à des fichiers et répertoires qui se trouvent en dehors du répertoire destiné. Cela permet de lire ou de modifier des fichiers sensibles du système, comme `/etc/passwd` sur un système Unix.

## Comment la trouver

### Vérifier s’il est possible de remonter dans d’autres répertoires :

- **Directement avec `../`** : Essayer d'utiliser cette séquence pour remonter dans l'arborescence des répertoires.

- **Via de l’encodage `"%2e%2e%2f"`** : Cette forme permet d’encoder la séquence de parenté `../` et pourrait contourner certaines protections.

- **Via les notations Unicode** : Par exemple, `%u2216%u2216` (code Unicode pour `../`) peut également contourner les mécanismes de filtrage.

Exemple dans notre cas de l'URL vulnérable :
http://192.168.56.3/index.php?page=../../../../../../../etc/passwd

Flag obtenu-> b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0

## Défenses insuffisantes

### 1. Routes imbriquées

La tentative de validation des chemins via des routes imbriquées peut être contournée si un attaquant encode ou double la séquence de parcours (`../`).

### 2. Paramètre de fichier dans une requête multipart/form-data

Certains mécanismes tentent de supprimer des séquences de parcours de répertoires en nettoyant les entrées utilisateur. Cela peut être contourné en encodant l’URL ou en doublant les caractères `../`.

Exemple : %2e%2e%2fet %252e%252e%252f

### 3. Validation de répertoire de base

Certains systèmes exigent que le nom de fichier commence par un répertoire de base spécifique, mais cette vérification peut être contournée en ajoutant une séquence de parcours de répertoire.

Exemple : /var/www/images/../../../etc/passwd

### 4. Validation d'extension de fichier

Une application peut exiger une extension de fichier spécifique (ex : `.png`), mais cela peut être contourné en utilisant un **octet nul** (`%00`) pour terminer le chemin avant l'extension attendue.

Exemple : filename=../../../etc/passwd%00.png

## Comment l'éviter

### 1. **Ne pas utiliser les entrées utilisateur directement pour appeler un fichier**

L'entrée utilisateur ne doit jamais être utilisée sans validation pour désigner des fichiers. Eviter les appels directs basés sur les entrées.

### 2. **Échapper et nettoyer les données utilisateurs**

Les données provenant des utilisateurs doivent être **encodées**, **échappées** et **nettoyées** pour éviter qu'elles ne soient interprétées comme du code exécutable.

### 3. **Validation stricte des entrées**

Les entrées des utilisateurs doivent être validées par rapport à une liste d’expressions autorisées. Si cela n'est pas possible, la validation doit confirmer que seules des chaînes sûres (par exemple, des caractères alphanumériques) sont autorisées.

### 4. **Utiliser une API de système de fichiers pour canoniser le chemin**

Après validation de l’entrée, ajoutez-la au répertoire de base et utilisez une API système pour obtenir un **chemin canonique** (normalisé). Ensuite, vérifiez que ce chemin canonique commence par le répertoire de base attendu.
