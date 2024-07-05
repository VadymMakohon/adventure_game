class Room:
    def __init__(self, name, description, exits, locked=False, puzzle=None, npc=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = []
        self.locked = locked
        self.puzzle = puzzle
        self.npc = npc

    def add_item(self, item):
        self.items.append(item)

    def take_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item
        return None

    def show_items(self):
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f" - {item.name}")
        else:
            print("There are no items here.")

    def solve_puzzle(self, answer):
        if self.puzzle and answer == self.puzzle['answer']:
            self.locked = False
            print("You solved the puzzle! The door is now unlocked.")
        else:
            print("That's not correct.")
    
    def interact_with_npc(self):
        if self.npc:
            self.npc.talk()
        else:
            print("There is no one here to talk to.")
