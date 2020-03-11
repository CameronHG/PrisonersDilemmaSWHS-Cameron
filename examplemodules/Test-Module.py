
import GLOBALS

c = GLOBALS.COLLUDE

b = GLOBALS.BETRAY

team_name='Test_Module'
strategy_name='Test_Strategy'
Strategy_description='''k'''


def move(my_history, their_history, my_score, their_score):

if 'b' in their_history[-4:]:
    return 'b'
else:
    if random.number() < 0.2
        return 'b'
    else:
        return 'c'
