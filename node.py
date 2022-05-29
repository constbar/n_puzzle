# make d type of arr np.array([[1,2,3], [4,5,6], [7,8,9]], int)   # init int
# все хранение идет в очередях
# сделать итератор __ит__ в классе для поиска конецного отца
from __future__ import annotations

import copy
import random
import collections
import numpy as np
# from scipy.spatial import distance
import utils





given = np.array([[1, 2, 3], [0, 8, 4], [7, 6, 5]]) # at the beggining
# given = np.array([[1, 8, 5], [0, 2, 4], [7, 6, 3]])
# given = np.array([[1, 2, 8], [3, 4, 5], [6, 7, 0]])
# given = np.array([[1, 2, 3], [0, 8, 4], [7, 6, 5]])

# given = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
# given = np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
# given = np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
# print(given)

# aim = np.array([[1,2,3], [4,5,6], [7,8,0]], int) # classic
aim = np.array([[1,2,3], [8,0,4], [7,6,5]], int)
# print('aim\n', aim)
# print('aim\n', aim)
# print('given\n', given)


directions: dict[str, int] = { # put in funcs (y, x) dict[funcs lol] # think ahere about it
	'up': lambda coordinate: (coordinate[0] - 1, coordinate[1]),
	'left': lambda coordinate: (coordinate[0], coordinate[1] - 1),
	'down': lambda coordinate: (coordinate[0] + 1, coordinate[1]),
	'right': lambda coordinate: (coordinate[0], coordinate[1] + 1)
	}
print(directions['up'].__name__)
print(directions['up']((1,2)))
print(type(lambda u : u))
print(type(1))

new_nodes = set() # deque!
"""
py - y coordinate of zero_coord
px - x coordinate of zero_coord
"""
zero_coord = np.where(given == 0) 
py: int = int(zero_coord[0])
px: int = int(zero_coord[1])

for calc_coord in directions.values():
	temp = np.copy(given)
	new_py, new_px = calc_coord((py, px))
	if new_py < 0 or new_px < 0:
		continue
	try:
		temp[py][px], temp[new_py][new_px] = temp[new_py][new_px], temp[py][px]
	except IndexError:
		continue
	# make labda func in other func
	# переделать на деку
	new_nodes.add(tuple(map(tuple, temp)))
# print(new_nodes)

size: int = 3



# print()
# print('manhten dist', utils.manhattan_distance(aim, given))
# print('euclide dist', utils.euclidean_distance(aim, given))
# print('euclide dist', utils.chebyshev_distance(aim, given))

class Solver:
	pass
	# openedlist = que
	# closedlsit = que


# hint
# import typing
import numpy.typing as npt
# numpy.ndarray[typing.Any, numpy.dtype[+ScalarType]]
# def foo(
#         hello: str='world', bar: str=None,
#         another_string_or_None: typing.Optional[str]=None):
# from __future__ import annotations

class Node:
	# def __init__(self, matrix=None, cost, level, father=None):
	# def __init__(self, cost, level, matrix: np.array = None, father: Node | int = None):
	# def __init__(self, cost, level, matrix: np.ndarray[int, Shape[size, size]] = None, father: Node | int = None):
	def __init__(self, cost, level, matrix: npt.NDArray[np.uint8] = None, father: Node = None):
		# self.__matrix = matrix
		# self.__level: int = level
		# self.__father: Node = father
		# self.__cost: int | float = cost
		self.__level: int = 0

a = Node(1,2)
print(a)
# class Node:
#     def __init__(self, father=None):
#         self.father = father
#         self.f = father.level # g
#         self.h = 0

x : npt.NDArray[np.float64] = np.array([1, 2, 3])