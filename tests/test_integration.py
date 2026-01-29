from lib.food import Food
from lib.menu import Menu

def test_add_to_menu_method():
    pizza = Food('pizza', 7.00)
    menu = Menu()
    menu.add_to_menu(pizza)
    assert menu.items == [pizza]

def test_get_menu_method():
    pizza = Food('pizza', 7.00)
    menu = Menu()
    menu.add_to_menu(pizza)
    assert menu.get_menu() == {'pizza': 7.00}

def test_get_menu_method_numerous_items():
    pizza = Food('pizza', 7.00)
    chips = Food('chips', 1.20)
    menu = Menu()
    menu.add_to_menu(pizza)
    menu.add_to_menu(chips)
    assert menu.get_menu() == {'pizza': 7.00, 'chips': 1.20}