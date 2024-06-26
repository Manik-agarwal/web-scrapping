import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://ticker.finology.in/"

r=requests.get(url)
print(r.status_code)

soup=BeautifulSoup(r.text,"lxml")

tb=soup.find("table",class_="table table-sm table-hover screenertable")
#print(tb)

headers=tb.find_all("th")
#print(headers)

titles=[]

for i in headers:
    titles.append(i.text)

#print(titles)

df=pd.DataFrame(columns=titles)
#print(df)


rows=tb.find_all("tr")
#
# print(rows)

rows1=[]

for i in rows[1:]:
    data=i.find_all("td")
    #print(data)
    row=[tr.text.strip() for tr in data]
    print(row)
    l=len(df)
    df.loc[l]=row
print(df)

df.to_csv("stock_ticker.csv")
