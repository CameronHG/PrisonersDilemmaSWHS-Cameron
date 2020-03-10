####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'HenryAndLillian'
strategy_name = 'Our Strategy is Winning'
strategy_description = 'Responses are based on the opponent. If that fails, tit-for-tat until both teams have colluded for 100 rounds in a row, then always betray.'


import GLOBALS

def move(my_history, their_history, my_score, their_score, opponent_name):

    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    if (opponent_name) == 'insertopponentnamehere':
        return 'c'
    else:
        if len(my_history) == 0:
            return GLOBALS.COLLUDE
        else:
            if 100 < len(my_history) and 'b' not in their_history[-100]:
                return GLOBALS.BETRAY
            else:
                if GLOBALS.BETRAY in their_history[-1]:
                    return GLOBALS.BETRAY
                if GLOBALS.COLLUDE in their_history[-1]:
                    return GLOBALS.COLLUDE





"""
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
"""
"""
import sys
import prisoners_dilemma
from loadfromdir import get_list_of_filenames
import os

should_rand = False
suppress_exceptions = False
modules = sys.argv
del modules[0]
updated_modules = []

for module_index in range(len(modules)):
    if modules[module_index] == '-d':
        assert (module_index + 1) < len(modules), "Got the dir flag with no argument"
        module_directory = modules[module_index + 1]
        assert os.path.isdir(module_directory), "There is no directory named {}".format(module_directory)
        if not (module_directory[-1] == '/'):
            module_directory += '/'
        add_to_modules = get_list_of_filenames(module_directory)
        for module in add_to_modules:
            updated_modules.append(module)
    elif modules[module_index - 1] == '-d':
        continue
    else:
        add_to_modules = modules[module_index]
        updated_modules.append(add_to_modules)

for module_path in updated_modules:
    assert os.path.isfile(module_path), "There is no file named {}".format(module_path)

prisoners_dilemma.main(updated_modules, should_rand, suppress_exceptions)
"""