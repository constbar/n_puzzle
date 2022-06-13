import collections

import sys
import numpy as np
import random

def create_random_puzzle(puzzle_size):
    rand = list(range(puzzle_size ** 2))
    random.shuffle(rand)
    rand = np.array(rand).reshape(puzzle_size, puzzle_size)
    return rand


def create_goal_puzzle(puzzle_size): # state reanme
    """	for snake/ulitka location"""
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

def parse_file(path): # or other name
    # params for choosing algo and count dist
    try:
        with open(path, 'r') as f: # path
            data = f.read().split('\n')
    except FileNotFoundError:
        sys.exit('need valid file')

    for i in data:
        if i.startswith('#'):
            data.remove(i)
        elif '#' in i:
            data[data.index(i)] = i[:i.find('#') - 1]
    if not data[0].strip().isdigit():
        sys.exit('er parsing')

    puzzle_size = int(data[0])
    del data[0]
    
    if puzzle_size != len(data):
        sys.exit('wrong declared size vs real size') # need to check it
    
    data = sum([i.split() for i in data], [])
    try:
        data = list(map(int, data))
    except ValueError:
        sys.exit('ints should be in data')

    
    if set(data) != set(range(puzzle_size ** 2)):
        sys.exit('wrong given args')

    # rename arr
    arr = np.array(data).reshape(puzzle_size, puzzle_size)
    return arr, puzzle_size # rename na puzzle i think


def gen_inversion_number(array):
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


def is_solvable(init_state, goal_state, width):
    init_inv = gen_inversion_number(sum(init_state.tolist(), []))
    goal_inv = gen_inversion_number(sum(goal_state.tolist(), []))
    if width % 2 == 0:
        start_zero_ind = int(np.where(init_state == 0)[0])
        goal_zero_ind = int(np.where(goal_state == 0)[0])
        return goal_inv % 2 == (init_inv + goal_zero_ind + start_zero_ind) % 2
    else:
        return init_inv % 2 == goal_inv % 2
