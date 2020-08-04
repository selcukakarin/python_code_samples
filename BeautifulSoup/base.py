import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/FB?p=FB'
response = requests.get(url)

html_icerik = response.content

soup = BeautifulSoup(html_icerik,'html.parser')

# print(soup.prettify())

for i in soup.find_all("a"):
    print(i.get("href"))
    print(i.text)
    print("*********************")

for i in soup.find_all("div"):
    print(i.text)
    print("*********************")