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
3. Run the game: `python3 game.py`

## Example Commands
- `north`: Move to the room to the north.
- `take key`: Pick up the key in the current room.
- `inventory`: Show your current inventory.
- `quit`: Exit the game.

## How to Run the Game

1. **Clone the Repository:**

   git clone <repository-url>
   cd adventure_game

2. **Run the game:**

   python3 game.py

## Adding Colors with colorama
In this modified code, the colorama library is used to add colors to the game text. Here are the color codes used:

- Fore.CYAN: Cyan color for room descriptions and help messages.
- Fore.YELLOW: Yellow color for input prompts.
- Fore.RED: Red color for error messages and locked doors.
- Fore.MAGENTA: Magenta color for puzzle questions.
- Fore.GREEN: Green color for successful actions (like taking or dropping an item). 

# Contributors
- [Vadym Makohon](https://github.com/VadymMakohon)
