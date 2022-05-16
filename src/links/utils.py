import requests
import lxml
from bs4 import BeautifulSoup


def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip().replace('-', '')

    price = soup.select_one(selector='#price_inside_buybox').getText()
    price = price.strip()
    price = float(price[1:])

    return name, price