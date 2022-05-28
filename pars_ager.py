import requests

from dotenv import load_dotenv

from bs4 import BeautifulSoup


load_dotenv('.env')



HEADERS = "HEADERS"

URL = "URL"



def get_html():
    respons = requests.get(url=URL, headers=HEADERS)
    with open("index.html", "w", encoding='utf-8-sig') as file:
        file.write(respons.text)


def open_file():
    with open("index.html", encoding='utf-8-sig') as file:
        src = file.read()
        return src


def get_cart():
    soup = BeautifulSoup(open_file(), "lxml")
    product_href = soup.find_all("div", class_="image")
    return product_href


def get_href():
    list_href = []
    for i in get_cart():
        href = i.find("a").get("href")
        list_href.append(href)
    return list_href



