from lib.todo_list import TodoList
from lib.todo import Todo

def test_add_todo_and_return_list_with_item():
    test_list = TodoList()
    test_todo_1 = Todo("task")
    test_list.add(test_todo_1)
    assert test_list.main_list == [test_todo_1]

def test_add_multiple_todos_and_return_list_with_items():
    test_list = TodoList()
    test_todo_1 = Todo("task 1")
    test_todo_2 = Todo("task 2")
    test_todo_3 = Todo("task 3")        
    test_list.add(test_todo_1)
    test_list.add(test_todo_2)
    test_list.add(test_todo_3)        
    assert test_list.main_list == [test_todo_1, test_todo_2, test_todo_3]

def test_return_incomplete_when_initialised():
    test_list = TodoList()
    test_todo_1 = Todo("task 1")
    test_todo_2 = Todo("task 2")
    test_todo_3 = Todo("task 3")        
    test_list.add(test_todo_1)
    test_list.add(test_todo_2)
    test_list.add(test_todo_3)        
    assert test_list.incomplete() == [test_todo_1, test_todo_2, test_todo_3]

def test_return_incomplete_when_one_completed():
    test_list = TodoList()
    test_todo_1 = Todo("task 1")
    test_todo_2 = Todo("task 2")
    test_todo_3 = Todo("task 3")        
    test_list.add(test_todo_1)
    test_list.add(test_todo_2)
    test_list.add(test_todo_3)
    test_todo_2.mark_complete()        
    assert test_list.incomplete() == [test_todo_1, test_todo_3]

def test_return_blank_list_when_all_completed():
    test_list = TodoList()
    test_todo_1 = Todo("task 1")
    test_todo_2 = Todo("task 2")
    test_todo_3 = Todo("task 3")        
    test_list.add(test_todo_1)
    test_list.add(test_todo_2)
    test_list.add(test_todo_3)
    test_todo_1.mark_complete()
    test_todo_2.mark_complete()  
    test_todo_3.mark_complete()        
    assert test_list.incomplete() == []

def test_return_one_item_when_one_item_out_of_three_complete():
    test_list = TodoList()
    test_todo_1 = Todo("task 1")
    test_todo_2 = Todo("task 2")
    test_todo_3 = Todo("task 3")        
    test_list.add(test_todo_1)
    test_list.add(test_todo_2)
    test_list.add(test_todo_3)
    test_todo_2.mark_complete()        
    assert test_list.complete() == [test_todo_2]

def test_no_items_complete_when_initialised():
    test_list = TodoList()
    test_todo_1 = Todo("task 1")
    test_todo_2 = Todo("task 2")
    test_todo_3 = Todo("task 3")        
    test_list.add(test_todo_1)
    test_list.add(test_todo_2)
    test_list.add(test_todo_3)       
    assert test_list.complete() == []

def test_give_up_puts_all_tasks_into_complete_list_and_off_incomplete():
    test_list = TodoList()
    test_todo_1 = Todo("task 1")
    test_todo_2 = Todo("task 2")
    test_todo_3 = Todo("task 3")        
    test_list.add(test_todo_1)
    test_list.add(test_todo_2)
    test_list.add(test_todo_3)
    test_list.give_up()       
    assert test_list.complete() == [test_todo_1,test_todo_2,test_todo_3]
    assert test_list.incomplete() == []