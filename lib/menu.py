
class Menu:

    def __init__(self):
        self.items = []

    def add_to_menu(self, item):
        self.items.append(item)

    def get_menu(self):
        return {item.get_name(): item.get_price() for item in self.items}