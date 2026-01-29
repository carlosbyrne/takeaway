from lib.menu import Menu
from unittest.mock import Mock

def test_initialisation_empty_list():
    menu = Menu()
    assert menu.items == []

def test_add_to_menu_method():
    menu = Menu()
    fake_food = Mock()
    menu.add_to_menu(fake_food)
    assert menu.items == [fake_food]


def test_get_menu_method():
    menu = Menu()
    fake_food = Mock()
    fake_food.item = 'pizza'
    fake_food.price = 5.00
    fake_food.get_name.return_value = fake_food.item 
    fake_food.get_price.return_value = fake_food.price 
    menu.add_to_menu(fake_food)
    assert menu.get_menu() == {'pizza': 5.00}

def test_get_menu_method_numerous_items():
    menu = Menu()
    fake_food1 = Mock()
    fake_food1.item = 'pizza'
    fake_food1.price = 5.00
    fake_food1.get_name.return_value = fake_food1.item
    fake_food1.get_price.return_value = fake_food1.price
    menu.add_to_menu(fake_food1)

    fake_food2 = Mock()
    fake_food2.item = 'chips'
    fake_food2.price = 1.20
    fake_food2.get_name.return_value = fake_food2.item
    fake_food2.get_price.return_value = fake_food2.price
    menu.add_to_menu(fake_food2)
    assert menu.get_menu() == {'pizza': 5.00, 'chips': 1.20}