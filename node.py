from __future__ import annotations

import copy
import random
import collections
import numpy as np
import numpy.typing as npt
import utils
from scipy.spatial import distance  # type: ignore

class Node:
    matrix_size = None
    calc_method = None
    goal_matrix = None
    algorithm = None
    aim_hash = None

    directions = {  # put in funcs (y, x) dict[funcs lol] # think here about it
        'up': lambda coordinate: (coordinate[0] - 1, coordinate[1]),
        'left': lambda coordinate: (coordinate[0], coordinate[1] - 1),
        'down': lambda coordinate: (coordinate[0] + 1, coordinate[1]),
        'right': lambda coordinate: (coordinate[0], coordinate[1] + 1)
    }

    def __init__(self, matrix, father):
        """make documentation here
        level means G(x)
        """
        self.matrix = matrix
        self.father = father
        self.level = 0 if father is None else father.level + 1

    def __hash__(self):
        return Node.make_matrix_hash(self.matrix)

    def __lt__(self, other):
        if Node.algorithm == 'a-star_search':
            return self.full_cost < other.full_cost
        elif Node.algorithm == 'greedy_search':
            return self.h_cost < other.h_cost
        else:
            return self.level < other.level

    def check_node_aim(self):
        return self.__hash__() == Node.aim_hash

    @property
    def zero_tile(self):
        zero_coord = np.where(self.matrix == 0)
        py: int = int(zero_coord[0])
        px: int = int(zero_coord[1])
        return py, px

    @property
    def h_cost(self):
        return sum([Node.calc_method(np.where(self.matrix == i),
                                     np.where(Node.goal_matrix == i))
                    for i in range(1, Node.matrix_size ** 2)])

    @property
    def full_cost(self):
        return self.level + self.h_cost

    def make_children(self):
        children_node_list = []
        py, px = self.zero_tile
        for calc_coord in self.directions.values():
            new_matrix = np.copy(self.matrix)
            new_py, new_px = calc_coord((py, px))
            if new_py < 0 or new_px < 0:
                continue
            try:
                new_matrix[py][px], new_matrix[new_py][new_px] = \
                    new_matrix[new_py][new_px], new_matrix[py][px]
            except IndexError:
                continue
            children_node_list.append(Node(new_matrix, self))
        return children_node_list

    def get_solution_path(self):
        solution_path = list()
        solution_path.append(self.matrix)
        while self.father is not None:
            solution_path.append(self.father.matrix)
            self.father = self.father.father
        return solution_path[::-1]

    @staticmethod
    def make_matrix_hash(matrix):
        return hash(tuple(map(tuple, matrix)))
