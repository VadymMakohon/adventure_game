class Player:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if not self.inventory:
            print("You have no items.")
        else:
            print("You have the following items:")
            for item in self.inventory:
                print(f"- {item.name}: {item.description}")
