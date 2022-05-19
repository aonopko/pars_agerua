from pars_ager import open_file, get_cart, get_href

from bs4 import BeautifulSoup


def test_open_file():
    with open("index.html", encoding='utf-8-sig') as file:
        src = file.read()
    assert open_file() == src


def test_get_cart():
    soup = BeautifulSoup(open_file(), "lxml")
    product_href = soup.find_all("div", class_="image")
    assert get_cart() == product_href


def test_get_href():
    list_href = []
    for i in get_cart():
        href = i.find("a").get("href")
        list_href.append(href)
    assert get_href() == list_href