import json

def save_game(player, current_room):
    game_state = {
        "player": player.__dict__,
        "current_room": current_room.name,
    }
    with open("savegame.json", "w") as f:
        json.dump(game_state, f)

def load_game(rooms):
    with open("savegame.json", "r") as f:
        game_state = json.load(f)
    player = Player(**game_state["player"])
    current_room = rooms[game_state["current_room"]]
    return player, current_room