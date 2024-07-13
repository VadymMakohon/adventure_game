import random
import time

def random_event(player):
    events = ["You found a hidden treasure!", "A trap was triggered! You lose 10 health.", "Nothing happens."]
    event = random.choice(events)
    print(event)
    if "lose 10 health" in event:
        player.take_damage(10)

def timed_event(player):
    time.sleep(30)  # Wait for 30 seconds
    print("A mysterious figure appears and gives you a clue!")
    player.add_score(5)  # Example of adding points for timed events