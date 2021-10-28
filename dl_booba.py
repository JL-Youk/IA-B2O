import requests
from bs4 import BeautifulSoup

b2o = open("b2o.txt", "a", encoding='utf-8')

urlbase = "https://www.paroles.net/";
URL = "https://www.paroles.net/booba"
page = requests.get(URL)

listes = BeautifulSoup(page.content, "html.parser")

listes = listes.find_all("table", class_="song-list")

for liste in listes:
    links = liste.find_all("a")
    for link in links:
        url_song = link.get("href");
        if urlbase in url_song:
            print("c'est pas du booba!")
        else:
            print("j'ai trouvé du booba!")
            url_song = urlbase+url_song
            print(url_song)
            page = requests.get(url_song)
            soup = BeautifulSoup(page.content, "html.parser")
            song = soup.find_all("div", class_="song-text")
            for parole in song:
                print("punchline trouvé !")
                punchline = parole.text.strip()
                print(punchline)
                b2o.write(punchline)
                b2o.write("\n")
b2o.close()
