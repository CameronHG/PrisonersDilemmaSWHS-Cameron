team_name = 'Huge Cash Prizes'
strategy_name = 'E'
strategy_description = 'Tit for Tat'

def move(my_history, their_history, my_score, their_score, opponent_name):

    if len(my_history) == 0:
        return 'c'
    elif their_history[-1] == 'c':
        return 'c'
    else:
        return 'b'