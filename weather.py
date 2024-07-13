import random

class Weather:
    def __init__(self):
        self.conditions = ["sunny", "rainy", "foggy", "stormy"]
        self.current_condition = random.choice(self.conditions)

    def change_weather(self):
        self.current_condition = random.choice(self.conditions)
        print(f"The weather has changed to {self.current_condition}.")
