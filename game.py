from rooms import Room
from player import Player
from items import Item
from npc import NPC
from quests import Quest
from events import random_event, timed_event
from save_load import save_game, load_game
from weather import Weather
from achievements import Achievement
from multiplayer import MultiplayerGame

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
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    rooms = {
        "kitchen": Room("Kitchen", "You are in a kitchen. There is a door to the north.", {"north": "hall"}),
        "hall": Room("Hall", "You are in a hall. There are doors to the south and east.", {"south": "kitchen", "east": "living_room"}),
        "living_room": Room("Living Room", "You are in a living room. There is a door to the west.", {"west": "hall"}),
    }

    current_room = rooms["kitchen"]

    npc = NPC("Bob", "Hello! I have a quest for you.")
    quest = Quest("Find the key", "Find the key hidden in the house.")

    weather = Weather()
    achievement = Achievement("First Step", "Take your first step in the game.")
    multiplayer = MultiplayerGame()
    multiplayer.add_player(player_name)

    while True:
        print(Colors.CYAN + current_room.description)
        print(f"Current weather: {weather.current_condition}")
        command = input(Colors.YELLOW + "> ").strip().lower()

        random_event(player)
        timed_event(player)

        if command in ["north", "south", "east", "west"]:
            if command in current_room.exits:
                current_room = rooms[current_room.exits[command]]
                if not achievement.is_unlocked:
                    print(achievement.unlock())
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
            print(Colors.CYAN + current_room.description)
        elif command == "talk":
            print(npc.talk())
        elif command == "quest":
            print(quest.description)
            if not quest.is_completed:
                quest.complete()
                player.add_score(10)
        elif command == "save":
            save_game(player, current_room)
            print(Colors.GREEN + "Game saved.")
        elif command == "load":
            player, current_room = load_game(rooms)
            print(Colors.GREEN + "Game loaded.")
        elif command == "weather":
            weather.change_weather()
        elif command == "players":
            multiplayer.list_players()
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
        elif command == "help":
            print(Colors.CYAN + "Available commands:")
            print(Colors.CYAN + " - north, south, east, west: Move in the specified direction.")
            print(Colors.CYAN + " - take [item]: Take an item from the room.")
            print(Colors.CYAN + " - drop [item]: Drop an item into the room.")
            print(Colors.CYAN + " - inspect [item]: Inspect an item in your inventory.")
            print(Colors.CYAN + " - look: Look around the room.")
            print(Colors.CYAN + " - inventory: Show your inventory.")
            print(Colors.CYAN + " - talk: Talk to an NPC.")
            print(Colors.CYAN + " - quest: Check your current quest.")
            print(Colors.CYAN + " - save: Save the game.")
            print(Colors.CYAN + " - load: Load the game.")
            print(Colors.CYAN + " - weather: Change the weather.")
            print(Colors.CYAN + " - players: List all players.")
            print(Colors.CYAN + " - help: Show this help message.")
            print(Colors.CYAN + " - quit: Quit the game.")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print(Colors.RED + "I don't understand that command.")

if __name__ == "__main__":
    main()
