from rooms import Room
from player import Player
from items import Item

def main():
    # Initialize game elements
    player = Player()
    rooms = {
        "kitchen": Room("Kitchen", "You are in a kitchen. There is a door to the north.", {"north": "hall"}),
        "hall": Room("Hall", "You are in a hall. There are doors to the south and east.", {"south": "kitchen", "east": "living room"}),
        "living_room": Room("Living Room", "You are in a living room. There is a door to the west.", {"west": "hall"}),
    }
    
    # Add items to rooms
    rooms["kitchen"].add_item(Item("key", "A small rusty key."))
    
    # Game loop
    current_room = rooms["kitchen"]
    while True:
        print(current_room.description)
        command = input("> ").strip().lower()
        
        if command in ["north", "south", "east", "west"]:
            if command in current_room.exits:
                current_room = rooms[current_room.exits[command]]
            else:
                print("You can't go that way.")
        elif command.startswith("take "):
            item_name = command[5:]
            item = current_room.take_item(item_name)
            if item:
                player.add_item(item)
                print(f"You took the {item.name}.")
            else:
                print(f"There is no {item_name} here.")
        elif command == "inventory":
            player.show_inventory()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()
