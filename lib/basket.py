from datetime import datetime
from datetime import timedelta
from random import randint

class Basket:

    def __init__(self):
        self.items = []
        self.checked_out = False

    def add_item(self, item):
        self.items.append(item)

    def get_receipt(self):
        receipt = {item.get_name(): item.get_price() for item in self.items}
        receipt_str = ""
        total = sum([price for price in receipt.values()])
        for food, price in receipt.items():
            formatted = f"{food.capitalize()}: £{price:.2f}, "
            receipt_str += formatted
        receipt_str = receipt_str[:-2]
        receipt_str += '. '
        receipt_str += f"Total: £{total:.2f}"
        return receipt_str

    def checkout(self):
        if self.checked_out:
            raise Exception("Already checked out.")
        if not self.items:
            raise Exception("Nothing in basket to check out.")
        
        checked_out = datetime.now()
        time_for_delivery = randint(25, 60)
        
        delivery_time = checked_out + timedelta(minutes=time_for_delivery)
        delivery_time_str = datetime.strftime(delivery_time, "%H:%M")
        
        confirmation_msg = f"Thank you! Your order was placed and will be delivered before {delivery_time_str}"
        self.checked_out = True
        return confirmation_msg