# make d type of arr np.array([[1,2,3], [4,5,6], [7,8,9]], int)   # init int
# все хранение идет в очередях
# сделать итератор __ит__ в классе для поиска конецного отца
# make folder for examples
# все свойства сделать приватными
from __future__ import annotations
# если нам не нужен геттер при сеттере, то можно его убрать???
# везде почистить сеттеры и геттеры где они не нужны
# directions: dict[str, int] = { # put in funcs (y, x) dict[funcs lol] # think ahere about it
# def __init__(self, father_level, matrix: npt.NDArray[np.uint16] = None, father: Node = None):
from parser import Solver

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
    aim_matrix = None
    aim_hash = None

    directions = {  # put in funcs (y, x) dict[funcs lol] # think here about it
        'up': lambda coordinate: (coordinate[0] - 1, coordinate[1]),
        'left': lambda coordinate: (coordinate[0], coordinate[1] - 1),
        'down': lambda coordinate: (coordinate[0] + 1, coordinate[1]),
        'right': lambda coordinate: (coordinate[0], coordinate[1] + 1)
    }

    def __init__(self, matrix, father):
        self.matrix = matrix
        self.father = father
        self.level = 0 if father is None else father.level + 1  # means G(x)

    def __hash__(self):
        return Node.make_matrix_hash(self.matrix)

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
                                     np.where(Node.aim_matrix == i)) for i in range(1, Node.matrix_size ** 2)])

    @property
    def full_cost(self):
        return self.level + self.h_cost

    def make_children(self):
        children_node_list = []
        py, px = self.zero_tile
        for calc_coord in self.directions.values():
            temp = np.copy(self.matrix) # rename new matrix
            new_py, new_px = calc_coord((py, px))
            if new_py < 0 or new_px < 0:
                continue
            try:
                temp[py][px], temp[new_py][new_px] = temp[new_py][new_px], temp[py][px]
            except IndexError:
                continue
            children_node_list.append(Node(temp, self))
        return children_node_list

    @staticmethod
    def make_matrix_hash(matrix):
        return hash(tuple(map(tuple, matrix)))
