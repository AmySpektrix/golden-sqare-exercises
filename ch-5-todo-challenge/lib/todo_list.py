class TodoList:
    def __init__(self):
        self.main_list = []

    def add(self, todo):
        return self.main_list.append(todo)

    def incomplete(self):
        return [task for task in self.main_list if task.complete==False]

    def complete(self):
        return [task for task in self.main_list if task.complete==True]
    
    def give_up(self):
        [task.mark_complete() for task in self.main_list]

