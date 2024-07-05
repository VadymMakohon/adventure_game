from rooms import Room
from player import Player
from items import Item

def main():
    # Initialize game elements
    player = Player()
    rooms = {
        "kitchen": Room("Kitchen", "You are in a kitchen. There is a door to the north.", {"north": "hall"}),
        "hall": Room("Hall", "You are in a hall. There are doors to the south and east.", {"south": "kitchen", "east": "living_room"}, locked=True, puzzle={"question": "What is 2+2?", "answer": "4"}),
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
                next_room = rooms[current_room.exits[command]]
                if next_room.locked:
                    print("The door is locked. Solve the puzzle to unlock it:")
                    print(next_room.puzzle['question'])
                    answer = input("> ").strip()
                    next_room.solve_puzzle(answer)
                if not next_room.locked:
                    current_room = next_room
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
        elif command.startswith("drop "):
            item_name = command[5:]
            item = player.remove_item(item_name)
            if item:
                current_room.add_item(item)
                print(f"You dropped the {item.name}.")
            else:
                print(f"You don't have a {item_name}.")
        elif command.startswith("inspect "):
            item_name = command[8:]
            item = player.get_item(item_name)
            if item:
                print(f"{item.name}: {item.description}")
            else:
                print(f"You don't have a {item_name}.")
        elif command == "look":
            current_room.show_items()
        elif command == "inventory":
            player.show_inventory()
        elif command == "help":
            show_help()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("I don't understand that command.")

def show_help():
    print("Available commands:")
    print(" - north, south, east, west: Move in the specified direction.")
    print(" - take [item]: Take an item from the room.")
    print(" - drop [item]: Drop an item into the room.")
    print(" - inspect [item]: Inspect an item in your inventory.")
    print(" - look: Look around the room.")
    print(" - inventory: Show your inventory.")
    print(" - help: Show this help message.")
    print(" - quit: Quit the game.")

if __name__ == "__main__":
    main()
