class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

puzzles = [
    Puzzle("What has keys but can't open locks?", "piano"),
    Puzzle("What runs but never walks?", "river"),
    Puzzle("What has a face and two hands but no arms or legs?", "clock"),
    Puzzle("What is full of holes but still holds water?", "sponge"),
    Puzzle("What gets wetter as it dries?", "towel")
]

import random

def get_random_puzzle():
    return random.choice(puzzles)