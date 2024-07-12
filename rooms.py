class Room:
    def __init__(self, name, description, exits, items=None, npcs=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items or {}
        self.npcs = npcs or {}

    def add_item(self, item):
        self.items[item.name] = item

    def take_item(self, item_name):
        return self.items.pop(item_name, None)

    def add_npc(self, npc):
        self.npcs[npc.name] = npc

    def get_npc(self, npc_name):
        return self.npcs.get(npc_name)

    def describe(self):
        print(self.description)
        for npc in self.npcs.values():
            print(f"You see {npc.name}.")
        for item in self.items.values():
            print(f"There is a {item.name} here.")
