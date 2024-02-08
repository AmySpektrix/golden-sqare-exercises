from lib.todo_list import TodoList

def test_initialise_list_and_return_blank_list():
    test_list = TodoList()
    assert test_list.main_list == []

def test_newly_initialised_list_has_blank_complete_list():
    test_list = TodoList()
    assert test_list.complete() == []   

def test_newly_initialised_list_has_blank_incomplete_list():
    test_list = TodoList()
    assert test_list.incomplete() == [] 
