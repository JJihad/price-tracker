from db.db_setup import create_database, create_items_table
from models.item import Item

# Create DB connection
connection = create_database()

# Create table if not exists
create_items_table(connection)

ac_black_flag = Item(url='https://store.playstation.com/fr-ca/product/UP0001-CUSA00010_00-AC4GAMEPS4000001', label='ac_black_flag', previous_lowest_price=100)
tom_clancy_wildlands = Item(url='https://store.playstation.com/en-ca/product/UP0001-CUSA02902_00-GRWNCSANORMAL000', label='tom_clancy_wildlands')
tom_clancy_breakpoint = Item(url='https://store.playstation.com/en-ca/product/UP0001-CUSA14405_00-GRW2SCEANORMAL00', label='tom_clancy_breakpoint', previous_lowest_price=100)

items_to_track = [ac_black_flag, tom_clancy_wildlands, tom_clancy_breakpoint]
inserted_items = [(item.url, item.label, item.previous_lowest_price_date, item.previous_lowest_price)
                  for item in items_to_track] 



    
connection.cursor().executemany('''INSERT INTO items (url,
                                label,
                                previous_lowest_price_date,
                                previous_lowest_price)
                                VALUES (?, ?, ?, ?)''', inserted_items)

connection.commit()

# Close connection
connection.close()