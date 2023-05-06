import requests as requ
from bs4 import BeautifulSoup as bs

## requesting the url based off user input

urlreq = input("url:")

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
}

site = requ.get(urlreq, headers=headers)

## format and save

soup = bs(site.text, "html.parser")

with open("index.html","w") as file:
    file.write(str(soup))

print("Sucsess") 