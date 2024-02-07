from lib.task_tracker import *
import pytest

"""
Given a new task tracker object is created
#see_todo_list returns a blank list
"""
def test_create_task_tracker_blank():
    task_tracker = Task_Tracker()
    with pytest.raises(Exception) as e:
        task_tracker.see_todo_list()
    assert str(e.value) == "No tasks to do yet."
"""
Given we have used #add_todo to add one new task to a blank list
#see_todo_list returns a list with "1: Task"
"""
def test_add_one_task():
    task_tracker = Task_Tracker()
    task_tracker.add_todo("Make cake")
    assert task_tracker.see_todo_list() == ["1: Make cake"]

"""
Given we have used #add_todo to add one new task to a non blank list
#see_todo_list returns a list with the previous task and the new task at the end "[1: Task , 2:Task2]"
"""
def test_add_multiple_tasks():
    task_tracker = Task_Tracker()
    task_tracker.add_todo("Make cake")
    task_tracker.add_todo("Eat cake")
    task_tracker.add_todo("Wash up cake plate")
    assert task_tracker.see_todo_list() == ["1: Make cake","2: Eat cake", "3: Wash up cake plate"]

"""
Given we have used #complete_todo with the task number to complete a task on a non blank list
we are informed which task we have completed.
"""
def test_remove_task_return_task_removed():
    task_tracker = Task_Tracker()
    task_tracker.add_todo("Make cake")
    task_tracker.add_todo("Eat cake")
    assert task_tracker.complete_todo(1)  == "Task Completed: Make cake"
# """
# Given we have used #complete_todo with the task number to complete a task on a non blank list "[1: Task , 2:Task2, 3:Task3]"
# #see_todo_list returns a list with the completed task [1] removed and the remaining tasks re-ordered "[1: Task2 , 2:Task3]"
# """

def test_remove_tasks_removes_from_list():
    task_tracker = Task_Tracker()
    task_tracker.add_todo("Make cake")
    task_tracker.add_todo("Eat cake")
    task_tracker.complete_todo(1)
    assert task_tracker.see_todo_list() == ["1: Eat cake"]