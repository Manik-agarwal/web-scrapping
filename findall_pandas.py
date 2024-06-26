import pandas as pd
import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")
names=soup.find_all("a",class_="title")
#print(names)

product_name=[]

for i in names:
    product_name.append(i.text)

#print(product_name)

prices = soup.find_all("h4",class_="price float-end card-title pull-right")

prices_list =[]

for i in prices:
    price=i.text
    prices_list.append(price)

#print(prices_list)

desc=soup.find_all("p",class_="description")

desc_list=[]

for i in desc:
    desc_list.append(i.text)
    
#print(desc_list)

review_list=[]

rev=soup.find_all("p",class_="review-count float-end")

for i in rev:
    review_list.append(i.text)

#print(review_list)

df=pd.DataFrame({"product Name":product_name,"prices":prices_list,"Description":desc_list,"number of riviews":review_list})
#print(df)

df.to_csv("products_details.csv")
