x# Task Tracker Recipe

## 1. Describe the Problem

<!-- User Stories -->

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

<!-- Questions to ask product owner: -->
    Do we want to be able to see completed tasks ever?
    - I am going to imagine no for these set of user stories but in reality probably yes.

    What form will tasks be presented?
    - As a string

    Do they need to appear in any order?
    - Assuming the order in which they are input

    How to mark tasks as complete? Do you need to type the full task or should they have a reference eg 1/2/3 etc
    - I think best to have some way of storing as both a list and then pulling a dictionary with the index of the list as well? For indicating wh

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._


```python

class Task_Tracker:
    # User-facing properties:
    #  todo_list = iterable object containing the todos

    def __init__(self):
        #Parameters: None
        #Side effects:
        #   Creates a blank todo_list
        pass

    def add_todo(self,todo:str):
        # Parameters:
        #   task: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass

    def see_todo_list(self):
        # Parameters:
        #   None
        # Returns:
        #   List of strings representing the todo's with a reference indicating the current index of the list
        # Side-effects
        #   Throws an exception if no todos are set
        pass
    
    def complete_todo(self, todo_index:int)
        # Parameters:
        #   Value number representing the task in the list
        # Returns:
        #   "{Task name} complete"
        # Side-effects
        #   Removes task from the list
        pass

``` 

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a new task tracker object is created
#see_todo_list returns a blank list
"""
task_tracker = Task_Tacker()
task_tracker.see_todo_list() # => # raises an error with the message "No tasks to do."

"""
Given we have used #add_todo to add one new task to a blank list
#see_todo_list returns a list with "1: Task"
"""
task_tracker = Task_Tacker()
task_tracker.add("Make cake")
task_tracker.see_todo_list() # => #["1: Make Cake"]

"""
Given we have used #add_todo to add one new task to a non blank list
#see_todo_list returns a list with the previous task and the new task at the end "[1: Task , 2:Task2]"
"""
task_tracker = Task_Tacker()
task_tracker.add("Make cake")
task_tracker.add("Eat cake")
task_tracker.see_todo_list() # => #["1: Make Cake","2: Eat Cake"]

"""
Given we have used #complete_todo with the task number to complete a task on a non blank list
we are informed which task we have completed.
"""
task_tracker = Task_Tacker()
task_tracker.add_todo("Make cake")
task_tracker.add_todo("Eat cake")
task_tracker.see_todo_list() # => #["1: Make Cake","2: Eat Cake"]

"""
Given we have used #complete_todo with the task number to complete a task on a non blank list "[1: Task , 2:Task2, 3:Task3]"
#see_todo_list returns a list with the completed task [1] removed and the remaining tasks re-ordered "[1: Task2 , 2:Task3]"
"""
task_tracker = Task_Tacker()
task_tracker.add_todo("Make cake")
task_tracker.add_todo("Eat cake")
task_tracker.complete_todo(1)
task_tracker.see_todo_list() # => #["1: Eat Cake"]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
