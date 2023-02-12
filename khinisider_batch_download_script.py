import requests
import bs4
import re
from urllib.parse import unquote
import os

url = "https://downloads.khinsider.com/game-soundtracks/album/the-house-in-fata-morgana-original-soundtrack"
r = requests.get(url)
urls_list = []
# print(r.text)
# print(r.content)
soup = bs4.BeautifulSoup(r.text, "html.parser")
for a in soup.findAll("a", href=True):
    if (re.findall("mp3", a['href'])):
        urls_list.append("https://downloads.khinsider.com" + a["href"])
        # print(f"URL: {a['href']}")
urls_list = list(set(urls_list))
for a in urls_list:
    pass
    # print(a)
print(f"Total number of songs = {len(urls_list)}")
# with open("Song_URLs.txt", "w") as f:
#     for a in urls_list:
#         f.write(a + "\n")
# """
with requests.Session() as req:
    for url in urls_list:
        r = req.get(url)
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        for a in soup.findAll("a", href=True):
            if (re.findall("mp3", a['href'])):
                filename = a["href"][a["href"].rfind("/")+1:]
                filename = unquote(unquote(filename))
                # filename = filename.replace("%2520", " ").replace("%20", " ").replace("%25", " ").replace("%C3", " ").replace("%A0", " ").replace("%25C3", "").replace("%2528", "").replace("%2529", "")
                print(filename)
                # print(f"URL: {a['href']}")
                if filename in os.listdir("Songs"):
                    continue
                mp3file = req.get(a["href"])
                # print(mp3file.status_code)
                if (mp3file.status_code == 200):
                    with open(f"Songs/{filename}", "wb") as f:
                        f.write(mp3file.content)
                else:
                    print(f"Unable to download {filename}")
# """