import re
import timeit
from queue import PriorityQueue
from typing import Optional, Dict, Any

import numpy as np
import pygame
from termcolor import colored

from node import Node


class Solver:
    __slots__ = (
        '__init_state', '__goal_state', '__puzzle_size',
        '__search_algo', '__heuristic_method', '__draw_solution',
        '__open_list', '__closed_list', '__search_time',
        '__moves_number', '__selected_states', '__size_complexity',
        '__solution', '__solution_path')

    def __init__(self, init_state: np.ndarray, goal_state: np.ndarray,
                 puzzle_size: int, algorithm: int = 0, heuristic: int = 0):
        self.__init_state = init_state
        self.__goal_state = goal_state
        self.__puzzle_size = puzzle_size
        self.__search_algo = [
            'a-star_search',
            'greedy_search',
            'uniform-cost_search'][algorithm]
        self.__heuristic_method = [
            Node.calc_manhattan_distance,
            Node.calc_euclidean_distance,
            Node.calc_chebyshev_distance][heuristic]

        self.__open_list: PriorityQueue[Node] = PriorityQueue()
        self.__closed_list: set[int] = set()

        self.__search_time = .0
        self.__moves_number = 0
        self.__selected_states = 0
        self.__size_complexity = 0

        self.__solve_puzzle()

    def __solve_puzzle(self) -> None:
        Node.goal_state = self.__goal_state
        Node.puzzle_size = self.__puzzle_size
        Node.algorithm = self.__search_algo
        Node.calc_method = self.__heuristic_method
        Node.goal_hash = Node.make_state_hash(self.__goal_state)
        Node.goal_coordinates = self.__make_goal_coordinates()

        self.__solution = self.__get_solution_node()
        if isinstance(self.__solution, Node):
            self.__solution_path = self.__solution.get_solution_path()
            self.__moves_number = len(self.__solution_path) - 1

    def __make_goal_coordinates(self) -> Dict[int, Any]:
        return {i: np.where(self.__goal_state == i) for i
                in range(1, self.__puzzle_size ** 2)}

    def __get_solution_node(self) -> Optional[Node | None]:
        start_time = timeit.default_timer()
        solution_node = None
        root_node = Node(self.__init_state, father=None)
        if root_node.is_goal_state() is True:
            solution_node = root_node
            self.__search_time = timeit.default_timer() - start_time
            return solution_node

        self.__open_list.put(root_node)
        while not self.__open_list.empty():
            lowest_cost_node = self.__open_list.get()
            self.__selected_states += 1
            children = lowest_cost_node.make_children()
            self.__closed_list.add(lowest_cost_node.__hash__())
            sum_memory_states = self.__open_list.qsize() + len(
                self.__closed_list) + len(children)
            if self.__size_complexity < sum_memory_states:
                self.__size_complexity = sum_memory_states
            for child in children:
                if child.is_goal_state():
                    solution_node = child
                    break
                elif child.__hash__() not in self.__closed_list:
                    self.__open_list.put(child)
            else:
                continue
            break
        self.__search_time = timeit.default_timer() - start_time
        return solution_node

    def print_solution_path(self) -> None:
        goal_state = self.__goal_state.tolist()
        len_path = self.__moves_number
        for state in self.__solution_path:
            print_matrix = state.copy()
            state = state.tolist()
            if isinstance(state, list):
                for y in range(self.__puzzle_size):
                    for x in range(self.__puzzle_size):
                        if state[y][x] == 0 and len_path > 0:
                            continue
                        elif isinstance(goal_state, list) \
                                and state[y][x] == goal_state[y][x]:
                            state[y][x] = colored(state[y][x], 'green')
                        else:
                            state[y][x] = colored(state[y][x], 'red')
                print_matrix = re.sub(r'\d+', '{}', print_matrix.__str__()). \
                    replace('[[', ' [').replace('[', '').replace(']', '')
                print(print_matrix.format(*tuple(sum(state, []))))
                print()
                len_path -= 1

    def show_result(self, *, visualize: bool) -> None:
        if visualize is True:
            self.__draw_result()
        else:
            self.__print_result()

    def __draw_result(self) -> None:
        black = (0, 0, 0)
        red = (247, 91, 72)
        green = (121, 247, 142)
        empty_tile = (219, 208, 200)
        pygame.init()
        window_size = 600
        square_size = int(window_size / self.__puzzle_size)
        window_size = square_size * self.__puzzle_size
        screen = pygame.display.set_mode((window_size, window_size))
        caption = f"{self.__puzzle_size ** 2 - 1} puzzle solution with " \
                  f"the {self.__search_algo.replace('_', ' ')} algorithm"
        pygame.display.set_caption(caption)
        digit_height = int(window_size / self.__puzzle_size * 0.6)
        font = pygame.font.Font('freesansbold.ttf', digit_height)

        i = 0
        run = True
        clock = pygame.time.Clock()
        while i < len(self.__solution_path) and run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

            screen.fill(black)
            for y in range(self.__puzzle_size):
                for x in range(self.__puzzle_size):
                    square = (y * square_size, x * square_size,
                              square_size - 1, square_size - 1)
                    if self.__solution_path[i][x][y] == 0:
                        pygame.draw.rect(screen, empty_tile, square)
                    elif self.__solution_path[i][x][y] == self.__goal_state[x][y]:
                        pygame.draw.rect(screen, green, square)
                    else:
                        pygame.draw.rect(screen, red, square)

                    if self.__solution_path[i][x][y] == 0:
                        text_surface_obj = font.render('', True, black)
                    else:
                        text_surface_obj = font.render(str(
                            self.__solution_path[i][x][y]), True, black)
                    text_rect_obj = text_surface_obj.get_rect()
                    text_rect_obj.center = (y * square_size + square_size / 2,
                                            x * square_size + square_size / 2)
                    screen.blit(text_surface_obj, text_rect_obj)
            pygame.display.update()
            pygame.time.wait(1000)
            clock.tick(20)
            i += 1
        pygame.quit()

    def __print_result(self) -> None:
        green = lambda i: colored(str(i), 'green')
        self.print_solution_path()
        # make variants here
        print('applied algorithm:', green(self.__search_algo.replace('_', ' ')))
        print('applied heuristic function:', green(' '.join(self.__heuristic_method.
                                                            __name__.split('_')[1:])))
        print()
        print('number of moves:', green(self.__moves_number))
        print('search time:', green(round(self.__search_time, 3)), 'secs')
        print('number of selected states:', green(self.__selected_states))
        print('number of states in memory:', green(self.__size_complexity))
