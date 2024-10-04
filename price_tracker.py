import requests as r
import bs4

def track_item_playstation_store(url: str) -> str:

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

print(track_item_playstation_store('https://store.playstation.com/fr-ca/product/UP0001-CUSA00010_00-AC4GAMEPS4000001'))
print(track_item_playstation_store('https://store.playstation.com/en-ca/product/UP0001-CUSA02902_00-GRWNCSANORMAL000'))
print(track_item_playstation_store('https://store.playstation.com/en-ca/product/UP0001-CUSA14405_00-GRW2SCEANORMAL00'))

