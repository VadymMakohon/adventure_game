class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.score = 0  # Initialize score

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                return item
        return None

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item.name}")

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None

    def take_damage(self, damage):
        self.health -= damage
        print(f"You took {damage} damage. Health is now {self.health}.")

    def add_score(self, points):
        self.score += points
        print(f"Score increased by {points}. Total score: {self.score}")

# Ensure you save this updated player.py file
