import re
import requests
from urllib.parse import unquote
import os

url = "https://downloads.khinsider.com/game-soundtracks/album/the-house-in-fata-morgana-original-soundtrack/201.%2520La%2520Realt%25C3%25A0%2520Nella%2520Nebbia.mp3"
filename = url[url.rfind("/")+1:]
# filename = re.sub("\%2520|\%25|\%20\s", "", filename)
# filename = filename.replace("%2520", "")
# re.sub("%", " ", filename)
# print(filename)

file = open("Song_URLs.txt", "r")
urls = []
for a in file:
    urls.append(a)
# print(a)

print(url)
expr = re.findall("%\w{4}", url)
print(expr)
expr = re.sub(re.compile("%\w{4}"), " ", url)
print(expr)
print(unquote(unquote(url)))
print(os.listdir("Songs"))


file.close()