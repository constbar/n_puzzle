import re
import sys
import utils
from node import Node
from queue import PriorityQueue
from scipy.spatial import distance
from termcolor import colored
import time

# add arg parse
# change comment in sys.exits
# maybe name shoud be n-puzzle.py
# funcion parsing send to utils
# elsi nepravilnij puzlle prishel -> input ues/no for generating own puzzle
# checker na validnost' puzzle solving
# rename file
# from solver import Solver
# можно сделть синглтоном
# need i puzzle size?
# size nd open and closed deques # 
# need size puzzle form parser
# closed list can be set и проверка может быть с помощью хеша
# можно сделать aim list или дикт и обращаться к функциям формирования по индексам
# make que in open list
# deq = deq c 1 start element
# проверить функцию дек на 
# def propery solved??

# for i in range(0, self.puzzle_size**2, self.puzzle_size):
# print(self.puzzle[i: i + self.puzzle_size])

# while queue: in solving loop
# queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
# кстати может быть генератором

# идем while -> добавляем детей -> проверка каждого на достижение цели -> если есть цель, 
# запускаем поиск отца

import colorama
import numpy as np

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

        self.init_node_cls_variables()
        self.solution = self.solve_puzzle()
        self.solution_path = self.solution.get_solution_path()
        self.print_solution_path()



    def init_node_cls_variables(self):
        Node.matrix_size = self.p_size
        Node.calc_method = self.method
        Node.aim_matrix = self.aim_puzzle
        Node.aim_hash = Node.make_matrix_hash(self.aim_puzzle)

    def solve_puzzle(self):
        solution_node = None
        root_node = Node(self.puzzle, father=None)
        if root_node.check_node_aim() is True:
            solution_node = root_node
            return solution_node

        self.open_list.put(root_node)
        while not self.open_list.empty():
            lowest_cost_node = self.open_list.get()
            # print('FULLcost lowest', lowest_cost_node.full_cost, '  and size', self.open_list.qsize())
            children = lowest_cost_node.make_children()
            self.closed_list.add(lowest_cost_node.__hash__())
            for child in children:
                if child.check_node_aim():
                    solution_node = child
                    break
                elif child.__hash__() not in self.closed_list:
                    self.open_list.put(child)
            else:
                continue
            break
        return solution_node

    def print_solution_path(self):
        aim = self.aim_puzzle.tolist()
        len_path = len(self.solution_path)
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
            if len_path > 1:
                print()
            len_path -= 1


if __name__ == '__main__':
    # sys.argv[1] = path
    path = 'tests/my_case.txt'
    data = utils.parse_file(path)
    solver = Solver(data)

