class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.health = 100
        self.inventory_limit = 5
        self.score = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("You have died.")
            # End game or restart logic
        else:
            print(f"You took {amount} damage. Health is now {self.health}.")

    def add_item(self, item):
        self.inventory[item.name] = item

    def remove_item(self, item_name):
        return self.inventory.pop(item_name, None)

    def get_item(self, item_name):
        return self.inventory.get(item_name)

    def show_inventory(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory.values():
                print(f"- {item.name}: {item.description}")
        else:
            print("Your inventory is empty.")

    def use_item(self, item_name):
        item = self.get_item(item_name)
        if item and hasattr(item, 'use'):
            item.use(self)
        else:
            print(f"You can't use {item_name}.")


    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"Your health is now {self.health}.")
