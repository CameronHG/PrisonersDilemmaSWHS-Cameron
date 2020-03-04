team_name = 'nayanwilllose'
strategy_name = 'Try not to lose'
strategy_description = "Do not lose"

def move(my_history, their_history, my_score, their_score, opponent_name):
    if my_score < -700:
        return 'c'
    elif len(their_history) > 0 and 'b' in their_history[-1]:
        return 'b'
    elif my_score < -1000 and 'b' in their_history[-1]:
        return 'b'



