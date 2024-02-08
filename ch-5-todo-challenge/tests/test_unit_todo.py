from lib.todo import Todo

def test_todo_initialises_with_properties_set():
    test_todo = Todo("test task 1")
    assert test_todo.task == "test task 1"
    assert test_todo.complete == False

def test_mark_complete_changes_complete_property_to_true():
    test_todo = Todo("test task 1")
    test_todo.mark_complete()
    assert test_todo.complete == True

