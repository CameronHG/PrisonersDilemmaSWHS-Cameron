team_name = 'nayanwilllose'
strategy_name = 'Try not to lose'
strategy_description = "Do not lose"

def move(my_history, their_history, my_score, their_score, opponent_name):
    if my_score < -700:
        return 'b'
    elif len(their_history) > 0 and 'b' in their_history[-1]:
        return 'b'
    elif my_score < -1000 and 'b' in their_history[-1]:
        return 'b'
    elif len(their_history) > 35 and 'b' in their_history < 5:
        return 'c'
    elif len(my_history) > 12 and len(my_history) <= 25 and len(their_history) > 12 and len(their_history) <= 25:
        sharks = their_history[-1]
        shark = my_history[-1]

        for round in range(len(my_history) - 1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
        if (prior_round_me == shark) and \
                (prior_round_them == sharks):
            return 'c'
    elif their_score < -400 and their_score > -750:
        return 'c'
    elif 'Ethan' in opponent_name and len(their_history) > 5 and their_history[-1]  == 'b' or my_history == '6':
        return 'b'
    elif 'HHHHHHH' in opponent_name and my_history[-1] == 'b':
        return 'b'
    elif 'Henry' in opponent_name:
        return 'b'
    elif 'Test' in opponent_name and 'b' in my_history[-4]:
        return 'b'
    elif 'Huge' in opponent_name and len(their_history) > 1 and my_history[-1] == 'c':
        return 'b'
    else:
        return 'c'








