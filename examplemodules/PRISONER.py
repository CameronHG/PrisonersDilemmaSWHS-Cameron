from numpy import random

team_name = 'Ethan and Oliver'
strategy_name = 'Ethan and Olivers CRAAZY STRATEGY!!!!'
strategy_description = 'A secret strargegy'


def move(my_history, their_history, my_score, their_score, opponent_name):
    tooManyBetrays = 0
    if their_history[-1:] == 'b':
        if their_history[-3:] == 'b':       # If opponent betrays 3 times in a row, start to only betray (see line 17)
            tooManyBetrays = 1
        else:                               # If opponent betrays once, betray next turn
            return 'b'
    elif their_history == 6:                # ALWAYS BETRAY ON ROUND SEVEMN!!!!!!!!!!!
        return 'b'
    elif tooManyBetrays == 1:
        return 'b'
    else:                                   # Otherwise, collude
        return 'c'