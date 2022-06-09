import re
import sys
import utils
from node import Node
from queue import PriorityQueue
from scipy.spatial import distance
from termcolor import colored
import timeit
import numpy as np

# __doc__ describes features
# print result can be caled outsisde class
# and print solution path


class Solver:
    __slots__ = (
        '__init_state', '__goal_state', '__puzzle_size',
        '__search_algo', '__heuristic_method', '__open_list',
        '__closed_list', '__search_time', '__moves_number',
        '__selected_states', '__size_complexity', '__solution',
        '__solution_path')

    def __init__(self, init_state, goal_state, puzzle_size, algorithm=0, heuristic=0):
        self.__init_state = init_state
        self.__goal_state = goal_state
        self.__puzzle_size = puzzle_size
        self.__search_algo = [
            'a-star_search',
            'greedy_search',
            'uniform-cost_search'][algorithm]
        self.__heuristic_method = [
            distance.cityblock,
            distance.euclidean,
            distance.chebyshev][heuristic]

        self.__open_list = PriorityQueue()
        self.__closed_list = set()

        self.__search_time = 0
        self.__moves_number = 0
        self.__selected_states = 0
        self.__size_complexity = 0

        # make start_solving private func
        self.__init_node_cls_variables()
        self.__solution = self.__solve_puzzle()
        self.__solution_path = self.__solution.get_solution_path()

        self.__moves_number = len(self.__solution_path) - 1
        self.print_result()

    def __init_node_cls_variables(self):
        Node.puzzle_size = self.__puzzle_size
        Node.calc_method = self.__heuristic_method  # euclidean_method call
        Node.goal_state = self.__goal_state
        Node.algorithm = self.__search_algo  # maybe rename
        Node.aim_hash = Node.make_state_hash(self.__goal_state)

    def __solve_puzzle(self):
        start_time = timeit.default_timer()
        solution_node = None
        root_node = Node(self.__init_state, father=None)
        if root_node.check_node_aim() is True:
            solution_node = root_node
            self.__search_time = timeit.default_timer() - start_time
            return solution_node  # print puzzle solution is already given

        self.__open_list.put(root_node)
        while not self.__open_list.empty():
            lowest_cost_node = self.__open_list.get()
            # print(lowest_cost_node.state) # DEL
            # print('H COST', lowest_cost_node.h_cost) # DEL
            # exit()
            self.__selected_states += 1
            # print('FULLcost lowest', lowest_cost_node.full_cost, '  and size', self.open_list.qsize())
            children = lowest_cost_node.make_children()
            self.__closed_list.add(lowest_cost_node.__hash__())
            sum_memory_states = self.__open_list.qsize() + len(
                self.__closed_list) + len(children)
            if self.__size_complexity < sum_memory_states:
                self.__size_complexity = sum_memory_states
            for child in children:
                if child.check_node_aim():
                    solution_node = child
                    break
                elif child.__hash__() not in self.__closed_list:
                    self.__open_list.put(child)
            else:
                continue
            break
        self.__search_time = timeit.default_timer() - start_time
        return solution_node

    def print_solution_path(self):
        aim = self.__goal_state.tolist()
        len_path = self.__moves_number
        for state in self.__solution_path:
            print_matrix = state.copy()
            state = state.tolist()
            for y in range(self.__puzzle_size):
                for x in range(self.__puzzle_size):
                    if state[y][x] == 0 and len_path > 0:
                        continue
                    elif state[y][x] == aim[y][x]:
                        state[y][x] = colored(state[y][x], 'green')
                    else:
                        state[y][x] = colored(state[y][x], 'red')
            print_matrix = re.sub(r'\d+', '{}', print_matrix.__str__()).\
                replace('[[', ' [').replace('[', '').replace(']', '')
            print(print_matrix.format(*tuple(sum(state, []))))
            print()
            len_path -= 1

    def print_result(self):
        green = lambda i: colored(str(i), 'green')
        self.print_solution_path()
        # make variants here
        print('applied algorithm:', green(self.__search_algo))  # optional
        print('applied heuristic function:', green('manhattan'))  # optional
        print()
        print('number of moves:', green(self.__moves_number))
        print('search time:', green(round(self.__search_time, 3)), 'secs')
        print('number of selected states:', green(self.__selected_states))
        print('number of states in memory:', green(self.__size_complexity))


# rename all variables here
# make argvars for options algo and heru
if __name__ == '__main__':
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
