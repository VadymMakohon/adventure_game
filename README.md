# Adventure Game

## Overview
Adventure Game is a simple text-based game where the player navigates through different rooms in a house. Each room may have items to pick up or dangers to avoid. The goal is to find a key and escape the house.

![preview](https://github.com/user-attachments/assets/8b39bf24-27ba-4954-9544-f081efcbbce5)

## How to Play
- Navigate through rooms by typing commands like north, south, east, or west.
- Pick up items by typing take <item>.
- View your inventory by typing inventory.
- Solve puzzles presented after each command to progress.
- Interact with NPCs using the talk command.
- Check your current quest status by typing quest.
- Change the weather using the weather command.
- Save and load your game with save and load commands.
- View the list of players in multiplayer mode with players.
- Quit the game by typing quit.

## Setup
1. Clone this repository.
2. Navigate to the directory: `cd adventure_game`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - On macOS and Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
5. Install the required packages: `pip install colorama`
6. Run the game: `python game.py`

## Example Commands
- `north: Move to the room to the north.
- take key: Pick up the key in the current room.
- inventory: Show your current inventory.
- look: Look around the room.
- drop [item]: Drop an item into the room.
- inspect [item]: Inspect an item in your inventory.
- talk: Talk to an NPC.
- quest: Check your current quest status.
- save: Save the game.
- load: Load the game.
- weather: Change the weather.
- players: List all players in multiplayer mode.
- help: Show available commands.
- quit: Exit the game.

## Features
- Interactive Puzzles: Solve puzzles to unlock new areas and progress in the game.
- NPC Interactions: Talk to NPCs to receive quests and clues.
- Complex Quests: Complete multi-step quests for rewards.
- Dynamic Weather: Experience changing weather conditions.
- Achievements: Unlock achievements as you progress.
- Multiplayer: Play with other players and see who else is in the game.


## Colors in the game
In this modified code, ANSI escape codes are used to add colors to the game text. Here are the color codes used:

- CYAN: Cyan color for room descriptions and help messages.
- YELLOW: Yellow color for input prompts.
- RED: Red color for error messages and locked doors.
- MAGENTA: Magenta color for puzzle questions.
- GREEN: Green color for successful actions (like taking or dropping an item). 

# Contributors
- [Vadym Makohon](https://github.com/VadymMakohon)
