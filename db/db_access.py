import datetime
from models.item import Item

def select_all_items(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items;") 
    
    # Fetch all rows from the executed query
    rows = cursor.fetchall()
    
    # Convert rows to Item objects
    items = [
        Item(id=row[0], url=row[1], label=row[2], previous_lowest_price_date=datetime.date.fromisoformat(row[3]), previous_lowest_price=row[4])
        for row in rows
    ]

    return items

# Function to update an item in the database
def update_item(conn, item_id, new_price):
    cursor = conn.cursor()
    
    # Prepare the UPDATE statement
    sql = '''
        UPDATE items
        SET previous_lowest_price = ?
        WHERE id = ?;
    '''
    # Execute the UPDATE statement with the new values
    cursor.execute(sql, (new_price, item_id))
    
    # Commit the changes
    conn.commit()