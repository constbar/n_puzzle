import utils
from solver import Solver

# rename all variables here
# make argvars for options algo and heru
if __name__ == '__main__':
    # vis = True
    vis = False
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
    solver.show_result(visualize=vis)  # true or false
