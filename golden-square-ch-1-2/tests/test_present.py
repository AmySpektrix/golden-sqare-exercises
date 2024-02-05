import pytest
from lib.present import *

"""
When new class initialised it should have a value of none
"""
def test_initialised_none():
    new_present = Present()
    assert new_present.contents == None

"""
When nothing is wrapped and you use wrap on an item it should "wrap" the item and add it to self.contents
"""
def test_wrapping_item():
    new_present = Present()
    new_present.wrap("gift") 
    assert new_present.contents == "gift"

"""
When something is already wrapped and you use wrap on an item it should throw an error
"""
def test_error_wrapping_two_items():
    new_present = Present()
    new_present.wrap("gift") 
    with pytest.raises(Exception) as e:
        new_present.wrap ("gift 2")
    assert str(e.value) == "An item has already been wrapped."

"""
When something is wrapped and you use unwrap on an item it should return the item which was wrapped
"""
def test_unwrapping_item():
    new_present = Present()
    new_present.wrap("gift") 
    assert new_present.unwrap() == "gift"

"""
When nothing is wrapped and you use unwrap on an item it should throw an error
"""
def test_error_unwrapping_none_item():
    new_present = Present()
    with pytest.raises(Exception) as e:
        new_present.unwrap()
    assert str(e.value) == "No contents have been wrapped."

"""
When something is already wrapped and you use wrap on an item it should not wrap the item
"""
def test_error_wrapping_two_items():
    new_present = Present()
    new_present.wrap("gift") 
    with pytest.raises(Exception) as e:
        new_present.wrap ("gift 2")
    assert new_present.unwrap() == "gift"
