team_name = 'huge cash prizes'
strategy_name = 'It Just Works'
strategy_description = 'It Just Works'

def move(my_history, their_history, my_score, their_score, opponent_name):

    if 'AH' in opponent_name:
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'
    if 'Oliver' in opponent_name:
        return 'c'
    if 'illia' in opponent_name:
        if 99 < len(my_history):
            return 'b'
        else:
            return 'c'
    if 'ayan' in opponent_name:
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'
    else:
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'
