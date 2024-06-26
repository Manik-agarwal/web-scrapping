import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/phones"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")

boxes=soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")

#print(len(boxes))

box=soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")[1]

name=box.find("p").text
print(name)

desc=box.find("p",class_="description").text
print(desc)

navbar=soup.find_all("ul",class_="nav flex-column",id="side-menu")[0]

text=navbar.find("li",class_="active")

print(text.text)


