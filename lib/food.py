class Food:

    def __init__(self, item: str, price: float):
        self.item = item
        self.price = price

    def get_name(self):
        return self.item

    def get_price(self):
        return self.price
   
