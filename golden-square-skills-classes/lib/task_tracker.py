class Task_Tracker:
    # User-facing properties:
    #  todo_list = iterable object containing the todos

    def __init__(self):
        #Parameters: None
        #Side effects:
        #   Creates a blank todo_list
        self.todo_list = []
        

    def add_todo(self,todo:str):
        # Parameters:
        #   task: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        self.todo_list.append(todo)

    def see_todo_list(self):
        # Parameters:
        #   None
        # Returns:
        #   List of strings representing the todo's with a reference indicating the current index of the list
        # Side-effects
        #   Throws an exception if no todos are set
        if self.todo_list == []:
            raise Exception ("No tasks to do yet.")
        else:
            indexed_list = [(f"{self.todo_list.index(task) +1 }: {task}") for task in self.todo_list]
            return indexed_list
    
    def complete_todo(self, todo_index:int):
        # Parameters:
        #   Value number representing the task in the list
        # Returns:
        #   "{Task name} complete"
        # Side-effects
        #   Removes task from the list
        task_number = todo_index-1
        return f"Task Completed: {self.todo_list.pop(task_number)}"