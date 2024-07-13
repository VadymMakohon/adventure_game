class Achievement:
    def __init__(self, name, description, is_unlocked=False):
        self.name = name
        self.description = description
        self.is_unlocked = is_unlocked

    def unlock(self):
        self.is_unlocked = True
        return f"Achievement '{self.name}' unlocked!"
