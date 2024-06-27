import requests
from bs4 import BeautifulSoup
import pandas as pd

Names=[]
Prices=[]
Reviews=[]
Description=[]


for i in range(1,11):
    url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r=requests.get(url)

    soup=BeautifulSoup(r.text,"lxml")

    box=soup.find("div",class_="DOjaWF gdgoEp")


    names=box.find_all("div",class_="KzDlHZ")





    #print(names)
    for i in names:
        n=i.text
        Names.append(n)
    #print(len(Names))

    prices=box.find_all("div",class_="Nx9bqj _4b5DiR")

    for i in prices:
        Prices.append(i.text)

    #print(len(Prices))

    desc=box.find_all("ul",class_="G4BRas")

    for i in desc:
        n=i.text
        Description.append(n)

    #print(len(Description))

    reviews=box.find_all("div",class_="XQDdHH")

    for i in reviews:
        rv=i.text
        Reviews.append(rv)

    #print(len(Reviews))

df=pd.DataFrame({"Product names":Names,"Prices":Prices,"Product Description":Description,"Reviews":Reviews})

df.to_csv("flipkart_mobiles.csv")



#print(df)