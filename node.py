# make d type of arr np.array([[1,2,3], [4,5,6], [7,8,9]], int)   # init int
# все хранение идет в очередях
# сделать итератор __ит__ в классе для поиска конецного отца
# make folder for examples
# все свойства сделать приватными
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
# print(directions['up'].__name__)
# print(directions['up']((1,2)))
# print(type(lambda u : u))
# print(type(1))

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


# def __init__(cls, *args, **kwargs):
#   cls._var = 5
#   @property
#   def var(cls):
#       return cls._var
    
#   @var.setter
#   def var(cls, value):
#       cls._var = value


class Node:
    @classmethod
    @property
    def aim_hash(cls):
        return None

    # def __init__(self, father_level, matrix: npt.NDArray[np.uint16] = None, father: Node = None):
    def __init__(self, matrix, father, father_level):
       # father может быть и не налл, тк всего используется 1 раз нулл
       self.level: int = 0 if father_level is None else father_level + 1
       self.matrix = matrix
       self.father = father

       self.matrix_hash = Node.make_matrix_hash(matrix)





        # porperrt for zero tile
        # лушче стоимость будет считать каждый сам
        # property на level
        # property на кост
        # property на dist # if dist == 0 or 0.0 то это успех

        # добаляем дитя в новый список только если его нет в сете просмотренных

    def make_child_and_send_to_open_list():
        pass

    @staticmethod
    def make_matrix_hash(matrix):
        return hash(tuple(map(tuple, matrix)))


    def __hash__(self):
        # hash # tuple(map(tuple, self.aim_puzzle))
        pass

    # def __eq__
    # print(tuple(map(tuple, self.aim_puzzle)))
    # cls.aim_hash
    # compare with hash aim


    # getter cost, для добавления в список

    # проверка дитя на соответсвие сразу
    # и с помощью __eq__

        # at first we should check matrices


# a = Node(1,2)
# print(a)
# class Node:
#     def __init__(self, father=None):
#         self.father = father
#         self.f = father.level # g
#         self.h = 0

# x : npt.NDArray[np.float64] = np.array([1, 2, 3])