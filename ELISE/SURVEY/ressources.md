Nom de la faille/Definition
FR: Absence de vérification côté serveur des valeurs envoyées par l'utilisateur
Cette faille implique le manque de validation côté serveur des données envoyées par l'utilisateur, permettant à un attaquant de soumettre des valeurs non vérifiées et d’obtenir un accès non autorisé à des informations sensibles.
EN: Lack of server-side validation of user input
This vulnerability involves the lack of server-side validation of user-submitted data, allowing an attacker to submit unvalidated values and gain unauthorized access to sensitive information.

Contexte spécifique / Overview
FR: Dans le cas présent, la page "/index.php?page=survey" permet à l'utilisateur de soumettre un formulaire, mais il n'y a pas de vérification côté serveur pour les valeurs envoyées, telles que "42" pour un champ select. En conséquence, un attaquant peut manipuler les données envoyées par POST sans aucune validation, ce qui lui permet d'obtenir un "flag" sans autorisation.
EN: In this case, the "/index.php?page=survey" page allows the user to submit a form, but there is no server-side validation for values sent, such as "42" for a select field. As a result, an attacker can manipulate the POST data without validation, allowing them to retrieve a "flag" without authorization.

Risques / Risks
FR: L'absence de validation côté serveur permet à un attaquant de soumettre des valeurs arbitraires, contournant ainsi la logique de contrôle de l'application. Cela pourrait mener à la fuite d'informations sensibles ou à l'exploitation de fonctionnalités restreintes à certains utilisateurs.
EN: The lack of server-side validation allows an attacker to submit arbitrary values, bypassing the application's control logic. This could lead to the leakage of sensitive information or exploitation of features restricted to certain users.

Comment la trouver / How it was discovered
FR: L'attaque a été réalisée en envoyant une requête POST avec une valeur non vérifiée, en utilisant cURL pour soumettre "sujet=2&valeur=42". La réponse de la page ne contenait aucune validation et a renvoyé directement le "flag".
EN: The attack was carried out by sending a POST request with an unchecked value, using cURL to submit "sujet=2&valeur=42". The page response did not perform any validation and directly returned the "flag".

Ressources/Outils:
- cURL : pour envoyer des requêtes POST manuelles
- grep : pour rechercher le "flag" dans la réponse
- Outils de développement du navigateur pour tester les requêtes manuelles

Flag : 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa

Comment l'éviter / How to fix it
FR:
- Valider toutes les entrées utilisateur côté serveur pour s'assurer que les données soumises sont dans les limites attendues.
- Implémenter une logique de vérification stricte sur les valeurs envoyées (ex. : s'assurer que les valeurs de champ de formulaire sont correctes et dans la plage valide).
- Limiter l'envoi de feedbacks à une seule fois par adresse IP ou par compte utilisateur connecté pour éviter l'exploitation multiple de la même soumission.
EN:
- Validate all user input server-side to ensure that submitted data is within the expected limits.
- Implement strict validation logic for sent values (e.g., ensure form field values are correct and within the valid range).
- Limit feedback submissions to once per IP address or logged-in user account to prevent multiple exploits of the same submission.
