# player.py
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

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item.name}: {item.description}")

    def take_damage(self, amount):
        self.health -= amount
        print(f"You took {amount} damage. Health is now {self.health}.")
        if self.health <= 0:
            print("You have died. Game over.")
            exit()

    def add_score(self, points):
        self.score += points
        print(f"Score increased by {points}. Total score: {self.score}")

    def show_score(self):
        print(f"Current score: {self.score}")
