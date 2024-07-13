import random

def random_event(player):
    events = [
        ("A trap was triggered! You lose 10 health.", lambda p: p.take_damage(10)),
        ("You found a health potion! You gain 10 health.", lambda p: p.take_damage(-10)),
    ]
    event, action = random.choice(events)
    print(event)
    action(player)

def timed_event(player):
    events = [
        ("A mysterious figure appears and gives you a clue!", lambda p: p.add_score(5)),
        ("You found a hidden treasure! Your score increases.", lambda p: p.add_score(10)),
    ]
    event, action = random.choice(events)
    print(event)
    action(player)
