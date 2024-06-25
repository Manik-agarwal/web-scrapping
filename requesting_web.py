#scrapping html data as text from the website


import requests

url="https://results.eci.gov.in/"
r=requests.get(url)

print(r.status_code)
print(r.text)

