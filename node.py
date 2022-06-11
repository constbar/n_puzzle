from __future__ import annotations

import numpy as np


# repalce funcions order
from typing import Callable


class Node:
    __slots__ = ('state', '__father', '__level')
    puzzle_size: int | None = None  # make here types
    # calc_method:  None = None
    calc_method: Callable[[tuple, tuple], int | float] | None = None  # can make more deteil
    goal_state: np.ndarray | None = None
    algorithm: str | None = None
    aim_hash: int | None = None
    goal_coordinates = None  # check all cars for using

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
        print(type(Node.aim_hash))
        exit()

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

    def __get_zero_tile(self):
        zero_coord = np.where(self.state == 0)
        py = int(zero_coord[0])
        px = int(zero_coord[1])
        return py, px

    @property # no need for h cost
    def h_cost(self):  # int or float
        heuristic_result = 0
        for i in range(1, Node.puzzle_size ** 2):
            state_coordinates = np.where(self.state == i)

            print(type(state_coordinates))
            print(type(Node.goal_coordinates[i]))
            print(state_coordinates)
            print(Node.goal_coordinates[i])
            # exit()
            heuristic_result += Node.calc_method(
                tuple(state_coordinates), Node.goal_coordinates[i])  # why tuple
        return heuristic_result

    @property
    def full_cost(self): #  it calls anopther by letter
        return self.__level + self.h_cost

    def make_children(self):
        children_node_list = []
        py, px = self.__get_zero_tile()
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

    @staticmethod
    def calc_manhattan_distance(state_coord, goal_coord):
        # print(type(state_coord))
        # print(type(goal_coord))
        # exit()
        return int(np.abs(goal_coord[0] - state_coord[0]) +
                   np.abs(goal_coord[1] - state_coord[1]))

    @staticmethod
    def calc_euclidean_distance(state_coord, goal_coord) -> float:
        return float((goal_coord[0] - state_coord[0]) ** 2 +
                     (goal_coord[1] - state_coord[1]) ** 2) ** .5

    @staticmethod
    def calc_chebyshev_distance(state_coord, goal_coord) -> int:
        return int(max(np.abs(goal_coord[0] - state_coord[0]),
                       np.abs(goal_coord[1] - state_coord[1])))

# def
