import requests
from bs4 import BeautifulSoup

baixa = requests.get("https://c.xkcd.com/random/comic/")

soup = BeautifulSoup(baixa.text,'html.parser')
url_img = soup.select('div#comic img')[0]('src')
print(url_img)
dowload_url = "https:{}".format(url_img)

print("baixando: {}...".format(dowload_url))

with open('xlcd-scrapped.png','wb') as image:
  image.write(requests.get(dowload_url).content)