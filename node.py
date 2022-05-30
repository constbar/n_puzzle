# make d type of arr np.array([[1,2,3], [4,5,6], [7,8,9]], int)   # init int
# все хранение идет в очередях
# сделать итератор __ит__ в классе для поиска конецного отца
# make folder for examples
from __future__ import annotations


import copy
import random
import collections
import numpy as np
# from scipy.spatial import distance
import numpy.typing as npt
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

class Node:
	# def __init__(self, matrix=None, cost, level, father=None):
	# def __init__(self, cost, level, matrix: np.array = None, father: Node | int = None):
	# def __init__(self, cost, level, matrix: np.ndarray[int, Shape[size, size]] = None, father: Node | int = None):
	
	def __init__(self, father_level, cost, matrix: npt.NDArray[np.uint16] = None, father: Node = None):
		self.__level: int = level
		self.__cost: int | float = cost
		self.__matrix = matrix
		self.__father: Node = father
		# porperrt for zero location
		# лушче стоимость будет считать каждый сам
		# property на level
		# property на кост
		# property на dist # if dist == 0 or 0.0 то это успех

		# добаляем дитя в новый список только если его нет в сете просмотренных

	def make_child_and_send to_open_list():
		pass

	# getter cost, для добавления в список

	# проверка дитя на соответсвие сразу
	# и с помощью __eq__

		# at first we should check matrices


a = Node(1,2)
print(a)
# class Node:
#     def __init__(self, father=None):
#         self.father = father
#         self.f = father.level # g
#         self.h = 0

x : npt.NDArray[np.float64] = np.array([1, 2, 3])