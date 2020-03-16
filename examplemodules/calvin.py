import random

team_name = 'AHHHHHHHHHHHHHHH'
strategy_name = 'even more: AHHHHHHHHHHHHHHHHHHHHHH'
strategy_description = 'exponential growth '


def move(my_history, their_history, my_score, their_score, opponent_name):
    b = 'b'
    c = 'c'
    rounds = len(my_history)
    if random.randint(rounds, 200) == 200:
        return b
    if b in their_history[:1]:
        return b
    else:
        if b not in their_history[:5]:
            return b
        else:
            return c