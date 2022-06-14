#!/usr/bin/python3
# rename all variables here
import utils
from solver import Solver
import random
import argparse
import sys
import utils
import numpy as np
from termcolor import colored
import time

if __name__ == '__main__':
    """
    parser = argparse.ArgumentParser(
        description='solving n-puzzles of any complexity')
    parser.add_argument('-f', '--file', type=str, required=False,
                        help='path to puzzle file')
    parser.add_argument('-s', '--size', type=int, required=False,
                        help='size of the puzzle\'s side')
    parser.add_argument('-algo', '--algorithm', required=False,
                        type=str, default='a-star',
                        choices=['a-star', 'greedy', 'uniform-cost'],
                        help='choice of algorithm to use')
    parser.add_argument('-heur', '--heuristic', required=False,
                        type=str, default='manhattan',
                        choices=['manhattan', 'euclidean', 'chebyshev'],
                        help='choice of heuristic function to use')
    parser.add_argument('-shuffle', default=100, required=False,
                        type=int, help='number of puzzle shuffles')
    parser.add_argument('-vis', '--visualization', required=False,
                        type=bool, default=False,
                        help='puzzle solution visualization')
    args = parser.parse_args()

    def print_error_exit(text: str) -> None:
        print(colored(str(text), 'red'))
        sys.exit(1)

    if args.file and (args.size or args.shuffle):
        print_error_exit('need to choose between submitting a puzzle '
                         'through a file and generating a puzzle')
    elif not args.file and not args.size:
        print_error_exit('need to submit a puzzle through a file or '
                         'generate using parameters')
    elif args.size < 2:
        print_error_exit('puzzle must be more than 1 tile')
    elif args.shuffle < 0:
        print_error_exit('number of shuffles must not be a negative number')
    elif args.shuffle > 1000:
        print(colored('not recommended to shuffle the puzzle too much '
                      'times due to cpu usage', 'yellow'))

    algo_choice = ['a-star', 'greedy', 'uniform-cost'].index(args.algorithm)
    heur_choice = ['manhattan', 'euclidean', 'chebyshev'].index(args.heuristic)

    if args.file:
        pass # read for file
        # generated_puzzle =
        # sys.argv[1] = path
        # path = 'tests/my_case.txt'
        # # puzzle, size = utils.parse_file(path)  # add size in dict + algo + heru

    else:
        generated_puzzle = np.array(utils.make_puzzle(
            args.size, args.shuffle)).reshape(args.size, args.size)
        # print(generated_puzzle)

    # сделать что было и какая цель в пазле и подписать что сгенерированый пазл не решаем или решаем
    
    goal_state = utils.create_goal_state(args.size)

    """
    goal_state = utils.create_goal_state(4)

    # print(f"{'generated state':<15}{'goal state':>10}",) # !
    import re
    state = goal_state.tolist()
    kek = re.sub(r'\d+', '{}', goal_state.__str__()). \
        replace('[[', ' [').replace('[', '').replace(']', '')
    print(kek)
    kek = kek.format(*tuple(sum(state, [])))
    print(kek)
    le = kek[:kek.find('\n') + 1] # tochno pravilno
    lll = len(le)

    print()
    print(le)
    print(lll)
    max_width = max(lll, len('generated'))


"""
    clear_print = lambda state: state.__str__().replace(
        '[[', ' [').replace('[', '').replace(']', '')

    print_gen = 'generated\n' + clear_print(generated_puzzle) + '\n'
    print_goal = 'goal\n' + clear_print(goal_state) + '\n'

    # print(print_gen[:print_gen.find('\n')])
    # text_width = max(len(print_goal[:print_goal.find('\n')]) * 2,1)
                     # len('generated'))
    # print('type print_goal =', type(print_goal))
    # exit()
    # text_width = 20
    # text_width =
    print(type(print_gen))
    text_width = max(max(list(map(len, list(map(
        str, goal_state.tolist()))))), len('generated'))

    # print(f"{'generated'} {'goal':>{text_width}}",)  # !
    for i in range(print_goal.count('\n')):
        goal_index_n = print_goal.find('\n')
        gen_index_n = print_gen.find('\n')

        # print(colored(print_goal[:goal_index_n], 'yellow'), sep='')
        # print(colored(print_gen[:gen_index_n], 'green'), sep='')
        print(f"{colored(print_gen[:gen_index_n], 'yellow')} "
              f"{colored(print_goal[:goal_index_n], 'green'):>{text_width}}")

        print_goal = print_goal[goal_index_n + 1:]
        print_gen = print_gen[gen_index_n + 1:]
    """
"""
    # print('generated_puzzle =\n', generated_puzzle)
    # print()
    # print('goal_state =\n', goal_state)
    exit()


    if utils.is_solvable(generated_puzzle, goal_state, args.size) is False:
        print_error_exit('received puzzle cannot be solved. try to make a new one')

    solver = Solver(generated_puzzle, goal_state, args.size, algo_choice, heur_choice)
    solver.show_result(visualization=args.visualization)

"""

# from subj
# parser.add_argument("-s", "--solvable", action="store_true", default=False, help="Forces generation of a solvable puzzle. Overrides -u.")
# 	parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle")
# 	parser.add_argument("-i", "--iterations", type=int, default=1000, help="Number of passes")