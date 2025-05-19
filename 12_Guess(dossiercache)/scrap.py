import requests
from bs4 import BeautifulSoup


visited = set() ## url deja visitees
results_file = "results.txt" ## nom du fichier de resultats

def find_flag(url):
    if url in visited:
        return
    visited.add(url)
    #si l'url a deja ete visitee on n'y retourne pas
    # sinon on l'ajoute a visited

    try:
        r = requests.get(url) ## requete http get sur url
        r.raise_for_status()
        ## on print si on a une erreur reseau ou http
    except Exception as e:
        print(f"Erreur sur {url} : {e}")
        return

#on parse le html avec beautiful soup et si le parsing echoue on quitte
    soup = BeautifulSoup(r.text, 'html.parser')
    if soup is None:
        return

#on recup tous les liens <a> de la page
    links = soup.find_all("a")
    for link in links:
        href = link.get('href')
        #On checke pour chaque lien si c vide ou ../ de l'arborescence et dans ce cas on skip
        if not href or href == "../":
            continue
        #on reconstruit l'url complet avec ce qu'on a trouve comme path
        full_url = requests.compat.urljoin(url, href)

		#si le lien pointe sur un readme on telecharge et on lit le contenu txt
        if href == "README":
            try:
                readme = requests.get(full_url)
                content = readme.text
                #la on "filtre" en verifiant qu'il n'y a pas les mots cles de blagues habituelles pour s'assurer que c'est bien un flag
                if all(x not in content for x in ["Demande", "Toujours", "Tu", "Non"]):
                    print(f"[FLAG trouvé] dans {full_url} :\n{content}\n")
                    with open(results_file, "a+") as f:
                        f.write(f"URL: {full_url}\n{content}\n\n")
                        # et si ca passe le filtre on dit que le flag a ete trouve et on l'ecrit dans le fichier results.txt

            except Exception as e:
                print(f"Erreur en lisant {full_url} : {e}")
       #on appelle en recursif pour faire tous les paths possibles
        else:
            find_flag(full_url)


url = "http://localhost:8080/.hidden/"
find_flag(url)
