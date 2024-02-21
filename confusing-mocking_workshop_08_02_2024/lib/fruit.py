class Fruit():
    def __init__(self, name, calory):
        self.name = name
        self.calory = calory

    def get_name(self):
        return self.name
    
    def get_calory(self):
        return f"There are {self.calory} calories in the {self.name}"