from __future__ import annotations

from typing import Dict, Any, Callable, Tuple, List

import numpy as np



class Node:
    __slots__ = ('__state', '__father', '__level')
    goal_state: np.ndarray | None = None
    puzzle_size: int | None = None
    algorithm: str | None = None
    calc_method: Callable[[tuple, tuple], int | float] | None = None
    goal_hash: int | None = None
    goal_coordinates: Dict[int, Any] | None = None

    directions = {
        'up': lambda coordinate: (coordinate[0] - 1, coordinate[1]),
        'left': lambda coordinate: (coordinate[0], coordinate[1] - 1),
        'down': lambda coordinate: (coordinate[0] + 1, coordinate[1]),
        'right': lambda coordinate: (coordinate[0], coordinate[1] + 1)
    }

    def __init__(self, state: np.ndarray, father: Node | None):
        """level shows here the cost of reaching
        the current node from the root. g(x)"""
        self.__state = state
        self.__father = father
        self.__level: int = 0 if father is None else father.__level + 1

    def is_goal_state(self) -> bool:
        return self.__hash__() == Node.goal_hash

    def make_children(self) -> List[Node]:
        children_node_list = []
        py, px = self.__get_zero_tile()
        for calc_coord in self.directions.values():
            new_state = np.copy(self.__state)
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

    def get_solution_path(self) -> List[np.ndarray]:
        solution_path = list()
        solution_path.append(self.__state)
        while self.__father is not None:
            solution_path.append(self.__father.__state)
            self.__father = self.__father.__father
        return solution_path[::-1]

    def __hash__(self) -> int:
        return Node.make_state_hash(self.__state)

    def __lt__(self, other: Node) -> bool:
        if Node.algorithm == 'a-star_search':
            return self.__calc_c_cost() < other.__calc_c_cost()
        elif Node.algorithm == 'greedy_search':
            return self.__calc_h_cost() < other.__calc_h_cost()
        else:
            return self.__level < other.__level

    def __get_zero_tile(self) -> tuple[int, int]:
        zero_coord = np.where(self.__state == 0)
        py = int(zero_coord[0])
        px = int(zero_coord[1])
        return py, px

    def __calc_h_cost(self) -> int | float:
        heuristic_result = .0
        if isinstance(Node.goal_coordinates, dict) and Node.puzzle_size is not None:
            for i in range(1, Node.puzzle_size ** 2):
                state_coordinates = np.where(self.__state == i)
                if Node.calc_method is not None:
                    heuristic_result += Node.calc_method(
                        tuple(state_coordinates), Node.goal_coordinates[i])
        return heuristic_result

    def __calc_c_cost(self) -> int | float:
        return self.__level + self.__calc_h_cost()

    @staticmethod
    def make_state_hash(state: np.ndarray) -> int:
        return hash(tuple(map(tuple, state)))

    @staticmethod
    def calc_manhattan_distance(state_coord: Tuple[np.ndarray, ...],
                                goal_coord: Tuple[np.ndarray, ...]) -> int:
        return int(np.abs(goal_coord[0] - state_coord[0]) +
                   np.abs(goal_coord[1] - state_coord[1]))

    @staticmethod
    def calc_euclidean_distance(state_coord: Tuple[np.ndarray, ...],
                                goal_coord: Tuple[np.ndarray, ...]) -> float:
        return float((goal_coord[0] - state_coord[0]) ** 2 +
                     (goal_coord[1] - state_coord[1]) ** 2) ** .5

    @staticmethod
    def calc_chebyshev_distance(state_coord: Tuple[np.ndarray, ...],
                                goal_coord: Tuple[np.ndarray, ...]) -> int:
        return int(max(np.abs(goal_coord[0] - state_coord[0]),
                       np.abs(goal_coord[1] - state_coord[1])))
