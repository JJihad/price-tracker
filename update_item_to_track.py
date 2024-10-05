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