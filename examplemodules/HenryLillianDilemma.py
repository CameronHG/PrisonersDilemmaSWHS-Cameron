####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Henry and Lillian'
strategy_name = 'our strategy is winning'
strategy_description = """\
Collude first round. Compare all rounds to the previous round and 
assume opponent will behave the same as the first time the previous 
round's result occurred. If the previous round's result never has 
happened, collude except after being severly punished."""


def move(my_history, their_history, my_score, their_score):
    """Make my move based on the history with this player.

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
    """
    if len(my_history) == 0:  # It's the first round: collude
        return 'c'
    else:
        # If there was a previous round just like the last one,
        # do whatever they did in the round that followed it

        # Reference last round
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]

        # Look at rounds before that one
        for round in range(len(my_history) - 1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            # If one matches
            if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                return their_history[round]
        # No match found
        if my_history[-1] == 'c' and their_history[-1] == 'b':
            return 'b'  # Betray if they were severely punished last time
        else:
            return 'c'  # Otherwise collude.






#!/usr/bin/python3
"""
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
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

