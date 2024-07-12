class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class HealingPotion(Item):
    def __init__(self):
        super().__init__("Healing Potion", "Heals you for 20 health points.")

    def use(self, player):
        player.heal(20)
        player.remove_item(self.name)
        print("You used a Healing Potion.")
