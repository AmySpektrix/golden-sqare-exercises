from lib.fruit import *

"""
Given a Fruit object is instantiated
It intantiates with a name.
"""
def test_fruit_instantiates_with_name():
    fruit = Fruit('apple', 5)

    actual = fruit.get_name() # => None
    expected = 'apple'

    assert actual == expected

"""
Given a Fruit object is instantiated
It intantiates with a name.
"""
def test_fruit_instantiates_with_calory():
    fruit = Fruit('kiwi', 10)

    actual = fruit.get_calory()
    expected = f"There are 10 calories in the kiwi"

    assert actual == expected