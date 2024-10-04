import datetime

class Item:
    def __init__(self,
                 url: str,
                 label: str = None,
                 previous_date_check: datetime.date = datetime.date.today(),
                 previous_price: str = None):
        self.label = label
        self.url = url
        self.previous_date_check = previous_date_check
        self.previous_price = previous_price