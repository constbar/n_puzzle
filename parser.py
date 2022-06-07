import re
import sys
import utils
from node import Node
from queue import PriorityQueue
from scipy.spatial import distance
from termcolor import colored
import timeit


class Solver:
    def __init__(self, puzzle):
        # check later if it really all vals needs me
        # yes, i will add __vars everywhere
        self.puzzle = puzzle
        self.p_size = len(puzzle)
        self.aim_puzzle = utils.create_aim_puzzle(self.p_size)

        self.open_list = PriorityQueue()
        self.closed_list = set()

        self.method = [distance.cityblock,
                       distance.euclidean,
                       distance.chebyshev][0]  # try other

        self.__search_time = 0
        self.__moves_number = 0
        self.__selected_states = 0
        self.__size_complexity = 0

        # make function for run solving
        self.init_node_cls_variables()
        self.solution = self.solve_puzzle()
        if self.solution:  # need i this check?
            self.solution_path = self.solution.get_solution_path()

        self.__moves_number = len(self.solution_path)
        self.print_result()

    def init_node_cls_variables(self):
        Node.matrix_size = self.p_size
        Node.calc_method = self.method  # euclidean
        Node.aim_matrix = self.aim_puzzle
        Node.aim_hash = Node.make_matrix_hash(self.aim_puzzle)

    def solve_puzzle(self):
        i = 0
        start_time = timeit.default_timer()
        solution_node = None
        root_node = Node(self.puzzle, father=None)
        if root_node.check_node_aim() is True:
            solution_node = root_node
            self.__search_time = timeit.default_timer() - start_time
            return solution_node  # print puzzle solution is already given

        self.open_list.put(root_node)
        while not self.open_list.empty():
            lowest_cost_node = self.open_list.get()
            self.__selected_states += 1
            # print('FULLcost lowest', lowest_cost_node.full_cost, '  and size', self.open_list.qsize())
            children = lowest_cost_node.make_children()
            self.closed_list.add(lowest_cost_node.__hash__())
            if self.__size_complexity < self.open_list.qsize() + len(self.closed_list) + len(children):
                self.__size_complexity = self.open_list.qsize() + len(self.closed_list) + len(children)
            for child in children:
                if child.check_node_aim():
                    solution_node = child
                    break
                elif child.__hash__() not in self.closed_list:
                    self.open_list.put(child)
            else:
                continue
            break
        self.__search_time = timeit.default_timer() - start_time
        return solution_node

    def print_solution_path(self):
        aim = self.aim_puzzle.tolist()
        len_path = self.__moves_number
        for matrix in self.solution_path:
            print_matrix = matrix.copy()
            matrix = matrix.tolist()
            for y in range(self.p_size):
                for x in range(self.p_size):
                    if matrix[y][x] == 0 and len_path > 1:
                        continue
                    elif matrix[y][x] == aim[y][x]:
                        matrix[y][x] = colored(matrix[y][x], 'green')
                    else:
                        matrix[y][x] = colored(matrix[y][x], 'red')
            print_matrix = re.sub(r'\d+', '{}', print_matrix.__str__()).\
                replace('[[', ' [').replace('[', '').replace(']', '')
            print(print_matrix.format(*tuple(sum(matrix, []))))
            # if len_path > 1: # unncesasary
            print()
            len_path -= 1

    def print_result(self):
        green = lambda i: colored(str(i), 'green')
        self.print_solution_path()
        # make variants here
        print('applied algorithm:', green('a star search'))  # optional
        print('applied heuristic function:', green('manhatan'))  # optional
        print()
        print('number of moves:', green(self.__moves_number))
        print('search time:', green(round(self.__search_time, 3)), 'secs')
        print('number states in memory:', green(self.__size_complexity))
        print('number of selected states:', green(self.__selected_states))





if __name__ == '__main__':
    # sys.argv[1] = path
    path = 'tests/my_case.txt'
    data = utils.parse_file(path)
    solver = Solver(data)

