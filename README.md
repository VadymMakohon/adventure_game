# Adventure Game

## Overview
Adventure Game is a simple text-based game where the player navigates through different rooms in a house. Each room may have items to pick up or dangers to avoid. The goal is to find a key and escape the house.

![Preview](https://github.com/VadymMakohon/adventure_game/assets/138728243/56533d1e-b991-4ac1-95c1-8b552cd742d1)

## How to Play
- Navigate through rooms by typing commands like `north`, `south`, `east`, or `west`.
- Pick up items by typing `take <item>`.
- View your inventory by typing `inventory`.
- Quit the game by typing `quit`.

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
- `north`: Move to the room to the north.
- `take key`: Pick up the key in the current room.
- `inventory`: Show your current inventory.
- `look`: Look around the room.
- `drop [item]`: Drop an item into the room.
- `inspect [item]`: Inspect an item in your inventory.
- `help`: Show available commands.
- `quit`: Exit the game.

## Colors in the game
In this modified code, the colorama library is used to add colors to the game text. Here are the color codes used:

- Fore.CYAN: Cyan color for room descriptions and help messages.
- Fore.YELLOW: Yellow color for input prompts.
- Fore.RED: Red color for error messages and locked doors.
- Fore.MAGENTA: Magenta color for puzzle questions.
- Fore.GREEN: Green color for successful actions (like taking or dropping an item). 

# Contributors
- [Vadym Makohon](https://github.com/VadymMakohon)
