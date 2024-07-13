class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.inventory_limit = 5
        self.score = 0

# Example of a multiplayer setup
class MultiplayerGame:
    def __init__(self):
        self.players = []

    def add_player(self, player_name):
        new_player = Player(player_name)
        self.players.append(new_player)
        print(f"Player {player_name} has joined the game.")

    def list_players(self):
        for player in self.players:
            print(player.name)
