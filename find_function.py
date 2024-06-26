import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r=requests.get(url)

#print(r)

soup=BeautifulSoup(r.text,"lxml")

print(soup.find("h4",{"class":"pull-right price"}))
desc=(soup.find("p",{"class":"description"}))
print(desc.string)

a=(soup.find("p",class_="description"))
print(a.string)




