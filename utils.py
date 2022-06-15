import collections
import random
import sys
from typing import List

import numpy as np
from termcolor import colored


def print_error_exit(text: str) -> None:
    print(colored(str(text), 'red'))
    sys.exit(1)


def create_goal_state(puzzle_size: int) -> np.ndarray:
    deq = collections.deque(range(1, puzzle_size**2))
    res = np.zeros((puzzle_size, puzzle_size), dtype=int)

    y, x = 0, 0
    circle = 1
    while deq:
        try:
            if res[y][x] == 0:
                res[y][x] = deq.popleft()
        except IndexError:
            if circle % 4 == 0:
                y += 1
            res = np.rot90(res)
            circle += 1
            x = 0
        x += 1

    while res[0][0] != 1:
        res = np.rot90(res)
    return res


def parse_file(path: str) -> tuple[np.ndarray, int]:
    try:
        with open(path, 'r') as file:
            data = file.read().split('\n')
            data = [i for i in data if i]
    except FileNotFoundError:
        print_error_exit('need a valid file')

    for i in data:
        if i.startswith('#'):
            data.remove(i)
        elif '#' in i:
            data[data.index(i)] = i[:i.find('#') - 1]
    if not data[0].strip().isdigit():
        print_error_exit('invalid data in file')

    puzzle_size = int(data[0])
    del data[0]
    
    if puzzle_size != len(data):
        print_error_exit('mismatch of the declared size and '
                         'the size of the puzzle in the file')
    
    data = sum([i.split() for i in data], [])
    try:
        data = list(map(int, data))  # make new variable clear_data
    except ValueError:
        print_error_exit('the data in the puzzle must be positive numbers')
    if set(data) != set(range(puzzle_size ** 2)):
        print_error_exit('incorrect data inside the puzzle')

    init_state = np.array(data).reshape(puzzle_size, puzzle_size)
    return init_state, puzzle_size


def is_solvable(init_state: np.ndarray, goal_state: np.ndarray, width) -> bool:
    def gen_inversion_number(array: List[int]) -> int:
        inversions = 0
        for i in range(len(array)):
            n = array[i]
            if n <= 1:
                continue
            j = i + 1
            while j < len(array):
                if 0 < array[j] < n:
                    inversions += 1
                j += 1
        return inversions

    init_state_list = init_state.tolist()
    goal_state_list = goal_state.tolist()
    if isinstance(init_state_list, list) and isinstance(goal_state_list, list):
        init_inv = gen_inversion_number(sum(init_state_list, []))
        goal_inv = gen_inversion_number(sum(goal_state_list, []))
        if width % 2 == 0:
            start_zero_ind = int(np.where(init_state == 0)[0])
            goal_zero_ind = int(np.where(goal_state == 0)[0])
            return goal_inv % 2 == (init_inv + goal_zero_ind + start_zero_ind) % 2
        else:
            return init_inv % 2 == goal_inv % 2
    return False


def make_puzzle(size: int, shuffle_num: int) -> np.ndarray:
    def shuffle_matrix(puzzle: List[int]) -> None:
        idx = puzzle.index(0)
        poss = []
        if idx % size > 0:
            poss.append(idx - 1)
        if idx % size < size - 1:
            poss.append(idx + 1)
        if idx / size > 0 and idx - size >= 0:
            poss.append(idx - size)
        if idx / size < size - 1:
            poss.append(idx + size)
        swi = random.choice(poss)
        puzzle[idx] = puzzle[swi]
        puzzle[swi] = 0

    solvable = random.choice([True, False])
    gen_puzzle = create_goal_state(size).tolist()
    if isinstance(gen_puzzle, list):
        gen_puzzle = sum(gen_puzzle, [])
    for _ in range(shuffle_num):
        shuffle_matrix(gen_puzzle)

    if not solvable:
        if gen_puzzle[0] == 0 or gen_puzzle[1] == 0:
            gen_puzzle[-1], gen_puzzle[-2] = gen_puzzle[-2], gen_puzzle[-1]
        else:
            gen_puzzle[0], gen_puzzle[1] = gen_puzzle[1], gen_puzzle[0]
    return gen_puzzle
