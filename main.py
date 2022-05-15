import requests
from bs4 import BeautifulSoup
import lxml


url = 'https://www.amazon.com/Newest-Plays-TATION-Version-Gaming-Console/dp/B0B11GWBWG/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept-Language": "en",
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")

name = soup.find_all('span', class_='a-price a-text-price a-size-medium apexPriceToPay')
print(name)