class Blender():
    def __init__(self):
        self.storage = []

    def add_fruit(self, fruit):
        self.storage.append(fruit)

    def make_juice(self):
        fruit_names = []
        for fruit in self.storage:
            fruit_names.append(fruit.get_name())
        return ", ".join(fruit_names) + " juice"
    
    def calculate_calory(self):
        total_calory = 0
        for fruit in self.storage:
            total_calory += fruit.calory
        return total_calory