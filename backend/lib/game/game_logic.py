import random
from enum import Enum


class Choice(str, Enum):
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'


def rock_paper_scissors(choice):

    game_key = {
        ('rock', 'rock'): "It's a tie.",
        ('rock', 'paper'): "You lost.",
        ('rock', 'scissors'): "You won!",
        ('paper', 'rock'): "You won!",
        ('paper', 'paper'): "It's a tie.",
        ('paper', 'scissors'): "You lost.",
        ('scissors', 'rock'): "You lost.",
        ('scissors', 'paper'): "You won!",
        ('scissors', 'scissors'): "'It's a tie.'",
    }

    choices = ['rock', 'paper', 'scissors']
    opponent_choice = choices[random.randrange(0, 2)]
    message = game_key[(choice, opponent_choice)]
    result = {'user_choice': choice, 'opponent_choice': opponent_choice, 'message': message}

    return result
