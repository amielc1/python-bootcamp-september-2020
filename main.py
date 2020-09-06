import requests
from bs4 import BeautifulSoup

url = 'https://www.ynet.co.il/home/0,7340,L-184,00.html'
r = requests.get(url)
soup = BeautifulSoup(r.text)
for link in soup.select('a.smallheader'):
    print(link.text)