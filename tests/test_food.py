from lib.food import Food

def test_initialisation():
    meal = Food('pizza', 7.99)
    assert meal.item == 'pizza'
    assert meal.price == 7.99

def test_get_name_method():
    meal = Food('pizza', 7.99)
    assert meal.get_name() == 'pizza'

def test_get_price_method():
    meal = Food('pizza', 7.99)
    assert meal.get_price() == 7.99

