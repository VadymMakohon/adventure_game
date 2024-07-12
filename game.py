from rooms import Room
from player import Player
from items import Item, HealingPotion
from npc import NPC

# ANSI escape codes for colors
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

def main():
    # Initialize game elements
    player = Player()

    # Define rooms with items and NPCs
    rooms = {
        "kitchen": Room("Kitchen", "You are in a kitchen. There is a door to the north.", {"north": "hall"}),
        "hall": Room("Hall", "You are in a hall. There are doors to the south and east.", {"south": "kitchen", "east": "living_room"}),
        "living_room": Room("Living Room", "You are in a living room. There is a door to the west.", {"west": "hall"})
    }

    # Add items to rooms
    rooms["kitchen"].add_item(HealingPotion())

    # Add NPCs to rooms
    npc = NPC("Old Man", "An old man with a long beard.", "Beware of the dragon in the living room!")
    rooms["hall"].add_npc(npc)

    # Puzzle question
    puzzle_solved = False

    def solve_puzzle():
        nonlocal puzzle_solved
        print(Colors.MAGENTA + "To enter the living room, solve this puzzle: What has keys but can't open locks?")
        answer = input(Colors.YELLOW + "> ").strip().lower()
        if answer == "piano":
            puzzle_solved = True
            print(Colors.GREEN + "Correct! You may enter the living room.")
        else:
            print(Colors.RED + "Incorrect. Try again.")

    current_room = rooms["kitchen"]
    while True:
        current_room.describe()
        command = input(Colors.YELLOW + "> ").strip().lower()

        if command in ["north", "south", "east", "west"]:
            if command in current_room.exits:
                if current_room.name == "Hall" and command == "east" and not puzzle_solved:
                    solve_puzzle()
                    if puzzle_solved:
                        current_room = rooms[current_room.exits[command]]
                else:
                    current_room = rooms[current_room.exits[command]]
            else:
                print(Colors.RED + "You can't go that way.")
        elif command.startswith("take "):
            item_name = command[5:]
            item = current_room.take_item(item_name)
            if item:
                player.add_item(item)
                print(Colors.GREEN + f"You took the {item.name}.")
            else:
                print(Colors.RED + f"There is no {item_name} here.")
        elif command == "inventory":
            player.show_inventory()
        elif command == "look":
            current_room.describe()
        elif command.startswith("drop "):
            item_name = command[5:]
            item = player.remove_item(item_name)
            if item:
                current_room.add_item(item)
                print(Colors.GREEN + f"You dropped the {item.name}.")
            else:
                print(Colors.RED + f"You don't have {item_name}.")
        elif command.startswith("inspect "):
            item_name = command[8:]
            item = player.get_item(item_name)
            if item:
                print(Colors.CYAN + f"{item.name}: {item.description}")
            else:
                print(Colors.RED + f"You don't have {item_name}.")
        elif command.startswith("use "):
            item_name = command[4:]
            player.use_item(item_name)
        elif command.startswith("talk to "):
            npc_name = command[8:]
            npc = current_room.get_npc(npc_name)
            if npc:
                npc.talk()
            else:
                print(Colors.RED + f"There is no one named {npc_name} here.")
        elif command == "help":
            print(Colors.CYAN + "Available commands:")
            print(Colors.CYAN + " - north, south, east, west: Move in the specified direction.")
            print(Colors.CYAN + " - take [item]: Take an item from the room.")
            print(Colors.CYAN + " - drop [item]: Drop an item into the room.")
            print(Colors.CYAN + " - inspect [item]: Inspect an item in your inventory.")
            print(Colors.CYAN + " - use [item]: Use an item from your inventory.")
            print(Colors.CYAN + " - talk to [npc]: Talk to an NPC in the room.")
            print(Colors.CYAN + " - look: Look around the room.")
            print(Colors.CYAN + " - inventory: Show your inventory.")
            print(Colors.CYAN + " - help: Show this help message.")
            print(Colors.CYAN + " - quit: Quit the game.")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print(Colors.RED + "I don't understand that command.")

if __name__ == "__main__":
    main()