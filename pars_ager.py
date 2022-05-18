import requests

from bs4 import BeautifulSoup

HEADERS = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
 }

URL = "https://ager.ua/women/zhenskie-dzhinsy/"



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
    list_url = []
    for i in get_cart():
        href = i.find("a").get("href")
        list_url.append(href)
    return list_url




