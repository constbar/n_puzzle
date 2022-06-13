#!/usr/bin/python3
# rename all variables here
# make argvars for options algo and heru
import utils
from solver import Solver
import random
import argparse
import sys
import utils
import numpy as np
from termcolor import colored

# try
# parser = argparse.ArgumentParser()
# other arguments
# parser.add_argument('--file', type=open, action=LoadFromFile)
# args = parser.parse_args()

# try 2
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument('file', type=argparse.FileType('r'))
# args = parser.parse_args()
# print(args.file.readlines())

# try 3
# required_pos.add_argument('dataset', help='path to dataset')
# required_nam.add_argument('-o', '--outfile', required=True,
#                           help='path to output file')
# optional.add_argument('-t', '--threads', type=int,
#                           !default=10,!  # INTERESTING
#                       help='number of CPUs to use. [default: %(default)s]')

# answer
# if args.prox and (args.lport is None or args.rport is None):
#     parser.error("--prox requires --lport and --rport.")
# couldnt be given together"

# whhat if file came
# print goal state and generated or read -> sleep

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='solving n-puzzles of any complexity')
    parser.add_argument('-f', '--file', type=str, required=False,
                        help='path to puzzle file')
    parser.add_argument('-s', '--size', type=int, required=False,
                        help='size of the puzzle\'s side')

    # print if puzle is solvable
    # heuristic
    # algo
    # iteraet num ||| if file ter dont need


    # parser.add_argument('--val',                  choises
    #                     choices=['a', 'b', 'c'],
    #                     help='Special testing value')
    #
    # args = parser.parse_args(sys.argv[1:])

    args = parser.parse_args()

    print()
    print('file', args.file)
    print('size', args.size)
    print('\nyou are entered')
    exit()
    """
    # group 1
    parser.add_argument("-q", "--query", help="query", required=False)
    parser.add_argument("-f", "--fields", help="field names", required=False)

    # group 2
    parser.add_argument("-a", "--aggregation", help="aggregation",
                        required=False)

    args = parser.parse_args()
    
    print(args.aggregation)
    if args.aggregation and (args.query or args.fields):
        print("-a and -q|-f are mutually exclusive ...")
        sys.exit(2)
    """
    exit()
    #
    #
    # if args.size < 2:
    #     sys.exit("size must be greater than or equal to 1")

    generated_puzzle = np.array(utils.make_puzzle(3)).reshape(3, 3)  # make random puzzle
    print()
    print(generated_puzzle)

    # if not args.solvable and not args.unsolvable:
    # # vis = True
    vis = False
    # if vis -> vis
    # esle print
    algo = 0
    hero = 0
    # sys.argv[1] = path
    # path = 'tests/my_case.txt'
    # puzzle, size = utils.parse_file(path)  # add size in dict + algo + heru
    goal = utils.create_goal_state(3)  # puz size
    if utils.is_solvable(generated_puzzle, goal, 3) is False:
        print(colored('the puzzle cannot be solved', 'red'))
        exit(1)
    print()
    # dtype = float
    # print(goal)
    solver = Solver(generated_puzzle, goal, 3, algo, hero)
    solver.show_result(visualization=True)  # true or false



# from subj
# parser.add_argument("-s", "--solvable", action="store_true", default=False, help="Forces generation of a solvable puzzle. Overrides -u.")
# 	parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle")
# 	parser.add_argument("-i", "--iterations", type=int, default=1000, help="Number of passes")