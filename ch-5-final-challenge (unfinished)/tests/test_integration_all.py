from lib.Task import Task
from lib.Diary import Diary
from lib.DiaryEntry import DiaryEntry

"""
given I want to start a diary, 
when I initialise a diary it starts with a blank list of diary entries
"""
def test_blank_diary_has_blank_diary_entry_list():
    test_diary = Diary()
    assert test_diary.diary_entries == []

"""
given I want to start a diary with a task list
when I initialise a diary it starts with a blank list of tasks
"""
def test_blank_diary_has_blank_task_list():
    test_diary = Diary()
    assert test_diary.task_list == []

"""
given I want to start a diary with a phone number list
when I initialise a diary it starts with a blank list of numbers
"""
def test_blank_diary_has_blank_numbers_list():
    test_diary = Diary()
    assert test_diary.numbers_list == []

"""
given I want to add an entry to my Diary
when I use the add_task function with the parameter of the task detail
it creates a new task and adds it to the task list
"""
def test_create_and_add_task_to_list():
    test_diary = Diary()
    test_diary.add_task("task details 1")
    assert test_diary.task_list == ["task details"]