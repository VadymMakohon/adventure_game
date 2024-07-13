class Quest:
    def __init__(self, name, description, is_completed=False):
        self.name = name
        self.description = description
        self.is_completed = is_completed

    def complete(self):
        self.is_completed = True
        return f"Quest '{self.name}' completed!"