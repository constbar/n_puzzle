# add arg parse
# change comment in sys.exits
# maybe name shoud be n-puzzle.py
# funcion parsing send to utils
# elsi nepravilnij puzlle prishel -> input ues/no for generating own puzzle
# checker na validnost' puzzle solving

import sys
import numpy as np
from solver import Solver

if __name__== '__main__':
    # sys.argv[1] = path
    path = 'tests/my_case.txt'

    puzzle_size = 0
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
    print('puz size', puzzle_size)
    del data[0]
    print(len(data))
    print(data)
    if puzzle_size != len(data):
        sys.exit('wrong declared size vs real size') # need to check it
    exit()
    data = sum([i.split() for i in data], [])

    try:
        data = list(map(int, data))
    except ValueError:
        sys.exit('ints should be in data')
    print(data)
    exit()
    
    if set(data) != set(range(puzzle_size ** 2)):
        sys.exit('wrong given args')

    import numpy as np
    arr = np.array(data).reshape(puzzle_size, puzzle_size)
    print(arr)
    print(data)

    # print('data: ', data)
    # print('file: ', f)

    # kek = Puzzle(data, puzzle_size)
    # print(kek)

