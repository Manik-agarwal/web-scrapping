import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.iplt20.com/auction"

r=requests.get(url)

#print(r)

soup=BeautifulSoup(r.text,"lxml")

table=soup.find("table",class_="ih-td-tab auction-tbl")

header=table.find_all("th")

titles=[]

for i in header:
    title=i.text
    titles.append(title)

#print(titles)

df=pd.DataFrame(columns=titles)
print(df)

rows=table.find_all("tr")

3#print(len(rows[1]))

for i in rows[1:]:
    data=i.find_all("td")
    row=[tr.text.strip() for tr in data]
    l=len(df)
    df.loc[l]=row
    
print(df)

df.to_csv("auction_stats_ipl2024.csv")






