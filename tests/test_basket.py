from lib.basket import Basket
from unittest.mock import Mock, patch
from datetime import datetime
from datetime import timedelta


def test_initalisation():
    basket = Basket()
    assert basket.items == []
    assert basket.checked_out == False

def test_add_item_method():
    basket = Basket()
    fake_food = Mock()
    basket.add_item(fake_food)
    assert basket.items == [fake_food]

def test_get_receipt_method():
    basket = Basket()

    fake_food1 = Mock()
    fake_food1.item = 'pizza'
    fake_food1.price = 5.00
    fake_food1.get_name.return_value = fake_food1.item
    fake_food1.get_price.return_value = fake_food1.price 
    basket.add_item(fake_food1)

    fake_food2 = Mock()
    fake_food2.item = 'chips'
    fake_food2.price = 2.75
    fake_food2.get_name.return_value = fake_food2.item
    fake_food2.get_price.return_value = fake_food2.price 
    basket.add_item(fake_food2)

    assert basket.get_receipt() == "Pizza: £5.00, Chips: £2.75. Total: £7.75"

@patch('lib.basket.randint')
@patch('lib.basket.datetime')
def test_checkout_method_valid(mock_datetime, mock_randint):
    basket = Basket()

    fake_food1 = Mock()
    fake_food1.item = 'pizza'
    fake_food1.price = 5.00
    fake_food1.get_name.return_value = fake_food1.item
    fake_food1.get_price.return_value = fake_food1.price 
    basket.add_item(fake_food1)

    fake_food2 = Mock()
    fake_food2.item = 'chips'
    fake_food2.price = 2.75
    fake_food2.get_name.return_value = fake_food2.item
    fake_food2.get_price.return_value = fake_food2.price 
    basket.add_item(fake_food2)

    mock_randint.return_value = 30
    time_string = "19:30"
    mock_datetime.now.return_value = datetime.strptime(time_string, '%H:%M')
    time_of_arrival = mock_datetime.now() + timedelta(minutes=mock_randint())
    
    mock_datetime.strftime.return_value = datetime.strftime(time_of_arrival, "%H:%M")

    confirmation_msg = "Thank you! Your order was placed and will be delivered before 20:00"

    assert basket.checkout() == confirmation_msg