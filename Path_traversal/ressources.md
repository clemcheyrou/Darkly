Sources :
https://owasp.org/www-community/attacks/Path_Traversal

Nom de la faille:
Path traversal

Comment la trouver:

Vérifier s’il est possible de remonter dans d’autres répertoires :
- directement avec ../
- via de l’encodage %2e%2e%2f
- via les notations unicode %u2216%u2216
	http://192.168.56.3/index.php?page=../../../../../../../etc/passwd

Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 

Defenses insuffisantes :\
1. nested route \\
2. filename paramètre d'une multipart/form-data requête peut supprimer toute séquence de parcours de répertoire => possible de contourner ce type de nettoyage en encodant URL ou en doublant le code ../
	-%2e%2e%2fet %252e%252e%252f
3. Une application peut exiger que le nom de fichier fourni par l'utilisateur commence par le dossier de base attendu => possible de contourner ce type de nettoyage en rajoutant a la suite une séquence de parcours de répertoire
	-/var/www/images/../../../etc/passwd
4.Une application peut exiger que le nom de fichier fourni par l'utilisateur se termine par une extension de fichier attendue, telle que .png => possible de contourner ce type de nettoyage 'utiliser un octet nul pour terminer le chemin d'accès avant l'extension requise 
	-filename=../../../etc/passwd%00.png

Comment vraiment l'éviter :
- Ne pas utiliser les entrées utilisateurs directement pour appeler un fichier.
- Les données utilisateurs ne doivent pas être interprétées. Elles doivent être encodées, échappées et nettoyées.
- Elles doivent être validées par rapport à une liste d’expressions autorisées. Si ce n’est pas possible, alors la validation doit confirmer qu’il n’y a que du contenu autorisé (par exemple que des caractères alphanumériques).
- Après avoir validé l'entrée fournie, ajoutez-la au répertoire de base et utilisez une API de système de fichiers de plateforme pour canoniser le chemin. Vérifiez que le chemin canonisé commence par le répertoire de base attendu.