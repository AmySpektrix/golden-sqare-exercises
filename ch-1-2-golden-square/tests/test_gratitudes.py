from lib.gratitudes import Gratitudes
"""
when "Gratitudes" initialises it should start an empty list
"""
def test_start_with_empty_list():
    empty_list = Gratitudes()
    assert empty_list.gratitudes == []

"""
When you add a multiple gratitudes to the list it should append to the list
""" 
def test_append_gratitude():
    grat_test = Gratitudes()
    grat_test.add("friends")
    grat_test.add("tasty food")
    grat_test.add("warmth")    
    assert grat_test.gratitudes == ["friends", "tasty food", "warmth"]

"""
when you format the gratitudes it formats appropriately
"""
def test_format_gratitude():
    grat_test = Gratitudes()
    grat_test.add("friends")
    grat_test.add("tasty food")
    grat_test.add("warmth")  
    assert grat_test.format() == "Be grateful for: friends, tasty food, warmth"
