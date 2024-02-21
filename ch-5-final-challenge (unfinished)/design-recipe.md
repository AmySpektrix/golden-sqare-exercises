# Diary with Todolist - Multi-Class Planned Design Recipe

## 1. Describe the Problem
```
As a user
So that I can record my experiences
I want to keep a regular diary

 - keep a record of diary entry and title
```
```
As a user
So that I can reflect on my experiences
I want to read my past diary entries

 - return diary entries content and title (individually or full diary?)
```
```
As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

- return diary entry which matches time available to 
```
```
As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
```
```
As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
```



## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌───────────────────────────┐    ┌───────────────────────────┐
│   New Diary:              │    │  Diary Entry              │
│  (top Level)              │    │  Properties:              │
│                           │    │   -Title                  │
│Properties                 │    │   -Content                │
│  -Diary List              ├────►   -list of phone numbers  │
│  -Task List               │    │                           │
│  -Phone number list       │    │  Functions                │
│                           │    │   -read()                 │
│                           │    │   -reading_time ()        │
│ Functions                 │    │                           │
│                           │    └───────────────────────────┘
│  -add_task(task)          │
│  -add_entry(title,content)│    ┌───────────────────────────┐
│  -read_entry(title)       │    │  Todo tasks               │
│  -read_best_entry(wpm,time)    │                           │
│  -see_tasks()             │    │  Properties               │
│  -read_all_entries()      ├────►   -Task                   │
│  -see_incomplete_tasks()  │    │   -Complete               │
│  -see_complete_tasks()    │    │                           │
│  -see_phone_numbers       │    │   Functions               │
└───────────────────────────┘    │    -mark_complete()       │
                                 │                           │
                                 └───────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   diary_entries = list of diary entries (Entry class objects)
    #   task_list = list of tasks (Task class objects)
    #   phone_number_list = list of phone numbers (extracted from diary entry when added)

    def __init__(self):
        # side effects:
        #   create above holding lists
        pass # No code here yet

    def add_task(self, task_details):
        # Parameters:
        #   task_details: string
        # Side-effects:
        #   creates an instance of a task with the task_details
        #   adds task to task_list
        # Returns:
        #   nothing
        pass # No code here yet

    def add_diary_entry(self, title, content):
        # Parameters:
        #   title: string
        #   content: string
        # Returns:
        #   creates an instance of a diary entry with the title/contents
        #   adds diary entry to diary entry list
        #   adds phone numbers to phone number list keyword
        pass # No code here yet

    def read_entry(self,entry):
        # Parameters:
        #   entry: 
    pass

    def read_all_entries(self):
        # Parameters:
        #   none
        # returns:
        #   list of entries in the format ["Title: Content"]
    pass

    def read_best_entry_for_time(self,wpm,time)
        # Parameters:
        #   wpm: integer representing words per minute
        #   time: integer representing minutes to read
        # returns:
        #   one entry in the format "Title: Content" which matches the above criteria
    pass

    def see_all_tasks(self)
        # Parameters:
        #   none
        # returns:
        #   list of tasks in the format  "Task" 
    pass

    def see_complete_tasks(self)
        # Parameters:
        #   none
        # returns:
        #   list of tasks where complete = True 
    pass

    def see_incomplete_tasks(self)
        # Parameters:
        #   none
        # returns:
        #   list of tasks where complete = False
    pass

    def see_all_numbers(self)
        # Parameters:
        #   none
        # returns:
        #   list of phone numbers from the main list    
    pass

class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   content: string
    #   list_of_phone_numbers: list of phone numbers extracted from string

    def __init__(self, title, content):
        # Parameters:
            #   title: string
            #   content: string
        # Side-effects:
        #   Sets the title and content properties
        #   Extracts phone numbers from string and adds to list of phone numbers list
        pass # No code here yet

    def reading_time(self,wpm):
        # Returns:
        #   an integer representing the number of minutes reqired to read the contents - rounded to the nearest minute
        pass # No code here yet

class Task:
    # User-facing properties:
    #   task: string
    #   complete: boolian    

    def __init__(self, task):
        # Parameters:
            #   task: string
        # Side-effects:
        #   Sets the task properties
        #   Sets the complete boolian to false
        pass # No code here yet    

    def mark_complete(self)
        # Side-effects:
        #   sets the complete boolian to True
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE



_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

