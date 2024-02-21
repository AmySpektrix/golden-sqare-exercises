from lib.Task import Task

class Diary:
    # User-facing properties:
    #   diary_entries = list of diary entries (Entry class objects)
    #   task_list = list of tasks (Task class objects)
    #   phone_number_list = list of phone numbers (extracted from diary entry when added)

    def __init__(self):
        self.diary_entries = []
        self.task_list = []
        self.numbers_list = []

    def add_task(self, task_details):
        print(task_details)
        task_details = Task(task_details)
        print(task_details)
        self.task_list.append(task_details)

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

    def read_best_entry_for_time(self,wpm,time):
        # Parameters:
        #   wpm: integer representing words per minute
        #   time: integer representing minutes to read
        # returns:
        #   one entry in the format "Title: Content" which matches the above criteria
        pass

    def see_all_tasks(self):
        # Parameters:
        #   none
        # returns:
        #   list of tasks in the format  "Task" 
        pass

    def see_complete_tasks(self):
        # Parameters:
        #   none
        # returns:
        #   list of tasks where complete = True 
        pass

    def see_incomplete_tasks(self):
        # Parameters:
        #   none
        # returns:
        #   list of tasks where complete = False
        pass

    def see_all_numbers(self):
        # Parameters:
        #   none
        # returns:
        #   list of phone numbers from the main list    
        pass
