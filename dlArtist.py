import requests
from bs4 import BeautifulSoup
import sys

artiste = sys.argv[1]
nb_musique = 0
print("Recherche de musique de l'artiste " + artiste)
fichier = open("lyrics/"+artiste+".txt", "a", encoding='utf-8')
fichier.truncate()
urlbase = "https://www.paroles.net/"

def explore_page(url,artiste):
    global nb_musique
    page = requests.get(url)
    listes = BeautifulSoup(page.content, "html.parser")
    listes = listes.find_all("table", class_="song-list")
    for liste in listes:
        links = liste.find_all("a")
        for link in links:
            url_song = link.get("href");
            if urlbase not in url_song:
                # print("j'ai trouvé du "+artiste+" !")
                url_song = urlbase+url_song
                # print(url_song)
                page = requests.get(url_song)
                soup = BeautifulSoup(page.content, "html.parser")
                for titre in soup.find_all("h2"):
                    titre = titre.text.strip()

                classes = ['py-4', 'Content_4','Content_3','Content_2','Content_1']
                for i in classes:
                    for div in soup.find_all("div", {'class': i}):
                        div.decompose()
                song = soup.find_all("div", class_="song-text")
                for parole in song:
                    for titre in parole.find_all("h2"):
                        titre = titre.text.strip()
                    soup.find('h2').decompose()
                    # print("punchline trouvé !")
                    punchline = parole.text.strip()
                    print(punchline)
                    nb_musique = nb_musique+1
                    print("################################################################################################")
                    print(titre + ", " + str(nb_musique)+ "eme musiques trouvé")
                    print("################################################################################################")
                    fichier.write(punchline)
                    fichier.write("\n")

URL = urlbase+artiste
explore_page(URL,artiste)
page = requests.get(URL)

listes = BeautifulSoup(page.content, "html.parser")

pages = listes.find_all("a", class_="pager-letter")

for page in pages:
    url_page = page.get("href")
    if artiste in url_page:
        explore_page(url_page,artiste)

fichier.close()
