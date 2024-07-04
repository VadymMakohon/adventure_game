class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def take_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item
        return None
