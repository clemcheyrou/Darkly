http://192.168.56.3/robots.txt
http://192.168.56.3/whatever/
htpasswd
root:437394baff5aa33daa618be47b75cb49 (= login:password)
md5 decrypt: qwerty123@

The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

Comment l'éviter:
Proteger htpasswd par un htaccess pour ne pas voir cette route (disallow pour le fichier robot ne suffit pas)