import requests
from bs4 import BeautifulSoup

url="https://results.eci.gov.in/"
r=requests.get(url)

#print(r.text)

soup =BeautifulSoup(r.text,"lxml")
print(soup)