from __future__ import annotations

import copy
import random
import collections
import numpy as np
import numpy.typing as npt
import utils
from scipy.spatial import distance


# repalce funcions order


class Node:
    __slots__ = ('state', '__father', '__level')
    puzzle_size = None
    calc_method = None
    goal_state = None
    algorithm = None
    aim_hash = None

    directions = {  # put in funcs (y, x) dict[funcs lol] # think here about it
        'up': lambda coordinate: (coordinate[0] - 1, coordinate[1]),
        'left': lambda coordinate: (coordinate[0], coordinate[1] - 1),
        'down': lambda coordinate: (coordinate[0] + 1, coordinate[1]),
        'right': lambda coordinate: (coordinate[0], coordinate[1] + 1)
    }

    def __init__(self, state, father):
        """make documentation here
        level means G(x)
        """
        self.state = state  # rename back __
        self.__father = father
        self.__level = 0 if father is None else father.__level + 1

    def __hash__(self):
        return Node.make_state_hash(self.state)

    def __lt__(self, other):
        if Node.algorithm == 'a-star_search':
            return self.full_cost < other.full_cost
        elif Node.algorithm == 'greedy_search':
            return self.h_cost < other.h_cost
        else:
            return self.__level < other.__level

    def check_node_aim(self):
        return self.__hash__() == Node.aim_hash

    @property
    def zero_tile(self):
        zero_coord = np.where(self.state == 0)
        py: int = int(zero_coord[0])
        px: int = int(zero_coord[1])
        return py, px

    @property
    def h_cost(self):
        total: float = 0  # make int
        from math import sqrt
        # create function to calculate Manhattan distance
        # def manhattan(a, b):
        #     return [abs(val1 - val2) for val1, val2 in zip(a, b)]
        #     # return sum(abs(val1 - val2) for val1, val2 in zip(a, b))
        #
        for i in range(1, Node.puzzle_size ** 2):
            temp = list(zip(np.where(self.state == i), np.where(Node.goal_state == i)))
            diff = lambda y: float(np.abs(y[0] - y[1]))  # if manh or chevushev to INT
            yyy = diff(temp[0])  # srazu plusovat' k total
            xxx = diff(temp[1])
            total += xxx + yyy
        # print('MY H COST', total)
        return total  # rename manh dist
        # return sum([Node.calc_method(np.where(self.state == i),
        #                              np.where(Node.goal_state == i))
        #             for i in range(1, Node.puzzle_size ** 2)])

    @property
    def full_cost(self):
        return self.__level + self.h_cost

    def make_children(self):
        children_node_list = []
        py, px = self.zero_tile
        for calc_coord in self.directions.values():
            new_state = np.copy(self.state)
            new_py, new_px = calc_coord((py, px))
            if new_py < 0 or new_px < 0:
                continue
            try:
                new_state[py][px], new_state[new_py][new_px] = \
                    new_state[new_py][new_px], new_state[py][px]
            except IndexError:
                continue
            children_node_list.append(Node(new_state, self))
        return children_node_list

    def get_solution_path(self):
        solution_path = list()
        solution_path.append(self.state)
        while self.__father is not None:
            solution_path.append(self.__father.state)
            self.__father = self.__father.__father
        return solution_path[::-1]

    @staticmethod
    def make_state_hash(state):
        return hash(tuple(map(tuple, state)))

# def
