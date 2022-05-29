# add arg parse
# change comment in sys.exits

import sys
import numpy as np
from puzzle import Puzzle

if __name__=='__main__':
    puzzle_size = 0
    # try here with file not found
    with open(sys.argv[1], 'r') as f:
        data = f.read().split('\n')

    for i in data:
        if i.startswith('#'):
            data.remove(i)
        elif '#' in i:
            data[data.index(i)] = i[:i.find('#') - 1]
    if not data[0].isdigit():
        sys.exit('er parsing')
    
    puzzle_size = int(data[0])
    del data[0]
    data = sum([i.split() for i in data], [])
    print(data)

    try:
        data = list(map(int, data))
    except ValueError:
        sys.exit('ints should be in data')
    print(data)
    
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

