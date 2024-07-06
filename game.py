from rooms import Room
from player import Player
from items import Item
from npc import NPC
from colorama import Fore, Back, Style, init

def main():
    # Initialize colorama
    init(autoreset=True)

    # Initialize game elements
    player = Player()
    rooms = {
        "kitchen": Room("Kitchen", "You are in a kitchen. There is a door to the north.", {"north": "hall"}),
        "hall": Room("Hall", "You are in a hall. There are doors to the south and east.", {"south": "kitchen", "east": "living_room"}, locked=True, puzzle={"question": "What is 2+2?", "answer": "4"}),
        "living_room": Room("Living Room", "You are in a living room. There is a door to the west.", {"west": "hall"}, npc=NPC("John", "Hello, adventurer! I have a quest for you.")),
    }
    
    # Add items to rooms
    rooms["kitchen"].add_item(Item("key", "A small rusty key."))
    
    # Game loop
    current_room = rooms["kitchen"]
    while True:
        print(Fore.CYAN + current_room.description)
        command = input(Fore.YELLOW + "> ").strip().lower()
        
        if command in ["north", "south", "east", "west"]:
            if command in current_room.exits:
                next_room = rooms[current_room.exits[command]]
                if next_room.locked:
                    print(Fore.RED + "The door is locked. Solve the puzzle to unlock it:")
                    print(Fore.MAGENTA + next_room.puzzle['question'])
                    answer = input(Fore.YELLOW + "> ").strip()
                    next_room.solve_puzzle(answer)
                if not next_room.locked:
                    current_room = next_room
            else:
                print(Fore.RED + "You can't go that way.")
        elif command.startswith("take "):
            item_name = command[5:]
            item = current_room.take_item(item_name)
            if item:
                player.add_item(item)
                print(Fore.GREEN + f"You took the {item.name}.")
            else:
                print(Fore.RED + f"There is no {item_name} here.")
        elif command.startswith("drop "):
            item_name = command[5:]
            item = player.remove_item(item_name)
            if item:
                current_room.add_item(item)
                print(Fore.GREEN + f"You dropped the {item.name}.")
            else:
                print(Fore.RED + f"You don't have a {item_name}.")
        elif command.startswith("inspect "):
            item_name = command[8:]
            item = player.get_item(item_name)
            if item:
                print(Fore.GREEN + f"{item.name}: {item.description}")
            else:
                print(Fore.RED + f"You don't have a {item_name}.")
        elif command == "look":
            current_room.show_items()
        elif command == "talk":
            current_room.interact_with_npc()
        elif command == "inventory":
            player.show_inventory()
        elif command == "help":
            show_help()
        elif command == "quit":
            print(Fore.CYAN + "Thanks for playing!")
            break
        else:
            print(Fore.RED + "I don't understand that command.")

def show_help():
    print(Fore.CYAN + "Available commands:")
    print(Fore.CYAN + " - north, south, east, west: Move in the specified direction.")
    print(Fore.CYAN + " - take [item]: Take an item from the room.")
    print(Fore.CYAN + " - drop [item]: Drop an item into the room.")
    print(Fore.CYAN + " - inspect [item]: Inspect an item in your inventory.")
    print(Fore.CYAN + " - look: Look around the room.")
    print(Fore.CYAN + " - talk: Talk to an NPC if one is present.")
    print(Fore.CYAN + " - inventory: Show your inventory.")
    print(Fore.CYAN + " - help: Show this help message.")
    print(Fore.CYAN + " - quit: Quit the game.")

if __name__ == "__main__":
    main()
