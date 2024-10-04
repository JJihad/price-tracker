import sqlite3
import datetime

# Register a custom adapter for datetime.date
def adapt_date(date):
    return date.isoformat()  # Convert date to ISO format string

# Register the adapter with sqlite3
sqlite3.register_adapter(datetime.date, adapt_date)

class Item:
    def __init__(self,
                 url: str,
                 label: str = None,
                 previous_lowest_price_date: datetime.date = datetime.date.today(),
                 previous_lowest_price: str = None):
        self.label = label
        self.url = url
        self.previous_lowest_price_date = previous_lowest_price_date
        self.previous_lowest_price = previous_lowest_price