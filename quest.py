# quests.py

class Quest:
    def __init__(self, title, description, steps):
        self.title = title
        self.description = description
        self.steps = steps
        self.current_step = 0
        self.is_completed = False

    def next_step(self):
        if self.current_step < len(self.steps):
            print(f"Quest Step {self.current_step + 1}: {self.steps[self.current_step]}")
            self.current_step += 1
        if self.current_step == len(self.steps):
            self.is_completed = True
            print(f"Quest '{self.title}' completed!")

    def complete(self):
        self.is_completed = True
        print(f"Quest '{self.title}' completed!")
