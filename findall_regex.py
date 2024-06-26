import re
import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

prices=soup.find_all(string= re.compile("Galaxy"))

print(prices)
