#!/usr/bin/python3
import argparse
import time

import numpy as np
from termcolor import colored

import utils
from solver import Solver

if __name__ == '__main__':
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

    if args.file and args.size:
        utils.print_error_exit('need to choose between submitting a puzzle '
                               'through a file and generating a puzzle')
    elif not args.file and not args.size:
        utils.print_error_exit('need to submit a puzzle through a file or '
                               'generate using parameters')
    elif args.size and args.size < 2:
    # elif isinstance(args.size, int) and args.size < 2:
        utils.print_error_exit('puzzle must be more than 1 tile')
    elif args.shuffle < 0:
    # elif args.size and args.shuffle < 0:
        utils.print_error_exit('number of shuffles must not be a negative number')
    elif args.shuffle > 1000:
        print(colored('not recommended to shuffle the puzzle too much '
                      'times due to cpu usage', 'yellow'))
    # if args shuffle and file -> just inform that

    algo_choice = ['a-star', 'greedy', 'uniform-cost'].index(args.algorithm)
    heur_choice = ['manhattan', 'euclidean', 'chebyshev'].index(args.heuristic)

    if args.file:
        received_puzzle, args.size = utils.parse_file(args.file)
    else:
        # args.shuffle = 100 if not args.shuffle else args.shuffle
        received_puzzle = np.array(utils.make_puzzle(
            args.size, args.shuffle)).reshape(args.size, args.size)

    goal_state = utils.create_goal_state(args.size)

    print_state = lambda state, color: colored(state.__str__().replace(
        '[[', ' [').replace('[', '').replace(']', ''), color)

    print('received puzzle to solve')
    print(print_state(received_puzzle, 'yellow'))
    print()
    print('final state puzzle solution')
    print(print_state(goal_state, 'green'))
    print()

    if utils.is_solvable(received_puzzle, goal_state, args.size) is False:
        utils.print_error_exit('received puzzle cannot be solved. try to make a new one')
    else:
        print(colored('the resulting puzzle can be solved!', 'green'))
        time.sleep(2)
    solver = Solver(received_puzzle, goal_state, args.size, algo_choice, heur_choice)
    solver.show_result(visualization=args.visualization)
