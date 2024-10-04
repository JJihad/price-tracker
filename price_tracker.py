import requests as r
import bs4
from models.item import Item

def item_price_from_playstation_store(url: str) -> str:

    response = r.get(url)
    soup = bs4.BeautifulSoup(response.text, features='html.parser')

    price_lines = soup.find_all(
        class_='psw-t-title-m',
        attrs={'data-qa': 'mfeCtaMain#offer0#finalPrice'})
    item_price = price_lines[0].text

    if item_price == 'Free':
        price_lines = soup.find_all(
        class_='psw-t-title-m',
        attrs={'data-qa': 'mfeCtaMain#offer1#finalPrice'})
        item_price = price_lines[0].text

    return item_price


