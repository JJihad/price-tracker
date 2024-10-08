import logging
import requests as r
import bs4
from db.db_setup import create_database, create_items_table
from db.db_access import select_all_items, update_item
from models.item import Item
from send_email import email_body, send_email

# Set the logging level & the log message format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create DB connection
connection = create_database()
logging.info('Connection open')

# Create table if not exists
create_items_table(connection)

all_tracked_items = select_all_items(connection)
logging.info('Items tracked : ' + str(all_tracked_items.__len__()))

def item_price_from_playstation_store(url: str) -> float:

    response = r.get(url)
    soup = bs4.BeautifulSoup(response.text, features='html.parser')

    price_lines = soup.find_all(
        class_='psw-t-title-m',
        attrs={'data-qa': 'mfeCtaMain#offer0#finalPrice'})
    if not price_lines:
        raise Exception('Price not found for article : ' + item.label)

    item_price = price_lines[0].text

    if item_price == 'Free':
        price_lines = soup.find_all(
        class_='psw-t-title-m',
        attrs={'data-qa': 'mfeCtaMain#offer1#finalPrice'})
        item_price = price_lines[0].text

    return float(item_price.replace("$", ""))

def check_if_new_lowest_price(item: Item) -> bool:
    logging.info('checking if there is a new price for item : ' + item.label + ' lower than : ' + "$" + str(item.previous_lowest_price))
    return item.previous_lowest_price > item_price_from_playstation_store(item.url)

list_of_sales = []
for item in all_tracked_items:
    if (item.previous_lowest_price == 0) or (check_if_new_lowest_price(item)):
        previous_price = item.previous_lowest_price
        actual_price = item_price_from_playstation_store(item.url)

        list_of_sales.append((item, previous_price, actual_price))

        item.previous_lowest_price = actual_price
        update_item(connection, item.id, item.previous_lowest_price)

if list_of_sales:
    body = email_body(list_of_sales)  
    send_email(
            'Price drop alert for ' + str(len(list_of_sales)) + ' items',
            body,
            'example@gmail.com')

# Close connection
connection.close()