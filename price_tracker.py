import logging
import requests as r
import bs4
import datetime
from db.db_setup import create_database, create_items_table
from models.item import Item

# Set the logging level & the log message format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create DB connection
connection = create_database()

# Create table if not exists
create_items_table(connection)

def select_all_items(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items;") 
    
    # Fetch all rows from the executed query
    rows = cursor.fetchall()
    
    # Convert rows to Item objects
    items = [
        Item(url=row[1], label=row[2], previous_lowest_price_date=datetime.date.fromisoformat(row[3]), previous_lowest_price=row[4])
        for row in rows
    ]

    return items

all_tracked_items = select_all_items(connection)


# Close connection
connection.close()

def item_price_from_playstation_store(url: str) -> float:

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

    return float(item_price.replace("$", ""))

def check_if_new_lowest_price(item: Item) -> bool:
    return item.previous_lowest_price > item_price_from_playstation_store(item.url)

for item in all_tracked_items:
    logging.info('checking if there is a new lower price for item : ' + item.label)
    if item.previous_lowest_price == 0:
        item.previous_lowest_price = item_price_from_playstation_store(item.url)
        # TODO : update item in db
        print(item.label + ' is a new item in the list, actual price updated is : ' + str(item.previous_lowest_price))

    elif check_if_new_lowest_price(item):
        # TODO : update item in db
        # TODO : send email alert
        print(item_price_from_playstation_store(item.url))