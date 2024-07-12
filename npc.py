class NPC:
    def __init__(self, name, description, dialog):
        self.name = name
        self.description = description
        self.dialog = dialog

    def talk(self):
        print(f"{self.name} says: {self.dialog}")
