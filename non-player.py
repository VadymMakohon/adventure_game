class NPC:
    def __init__(self, name, dialog):
        self.name = name
        self.dialog = dialog

    def talk(self):
        print(self.dialog)
