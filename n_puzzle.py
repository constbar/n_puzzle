from solver import Solver
import utils

# rename all variables here
# make argvars for options algo and heru
if __name__ == '__main__':
    # if vis -> vis
    # esle print
    algo = 0
    hero = 0
    # sys.argv[1] = path
    path = 'tests/my_case.txt'
    puzzle, size = utils.parse_file(path)  # add size in dict + algo + heru
    goal = utils.create_goal_puzzle(size)  # puz size
    if utils.is_solvable(puzzle, goal, size) is False:
        print('wrong puz not ok')  # ex it in red
        exit()
    print()
    # dtype = float
    # print(goal)
    solver = Solver(puzzle, goal, size, algo, hero)