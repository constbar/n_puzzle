import utils
from node import Node
import sys

# add arg parse
# change comment in sys.exits
# maybe name shoud be n-puzzle.py
# funcion parsing send to utils
# elsi nepravilnij puzlle prishel -> input ues/no for generating own puzzle
# checker na validnost' puzzle solving
# rename file
# from solver import Solver
# можно сделть синглтоном
# need i puzzle size?
# size nd open and closed deques # 
# need size puzzle form parser
# closed list can be set и проверка может быть с помощью хеша
# можно сделать aim list или дикт и обращаться к функциям формирования по индексам
# make que in open list
# deq = deq c 1 start element
# проверить функцию дек на 
# def propery solved??

# for i in range(0, self.puzzle_size**2, self.puzzle_size):
# print(self.puzzle[i: i + self.puzzle_size])

# while queue: in solving loop
# queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
# кстати может быть генератором

# идем while -> добавляем детей -> проверка каждого на достижение цели -> если есть цель, 
# запускаем поиск отца



class Solver:
    def __init__(self, puzzle, puzzle_size):
        
        self.aim_puzzle = utils.create_aim_puzzle(puzzle_size)

        self.puzzle = puzzle
        self.puzzle_size = puzzle_size

        self.root_node = self.make_root_node()

        self.open_list = list()
        self.closed_list = set()

        # print(self.root_node)
        # print(self.root_node.level)
        # print(self.root_node.father)
        # print(self.root_node.matrix)


    def make_root_node(self):
        root = Node(self.puzzle, father=None, father_level=None)
        root.level = 0 # make setter
        Node.aim_hash = Node.make_matrix_hash(self.aim_puzzle)
        print(Node.aim_hash)
        root.__eq__(22)

        # проверяем?

        # добавляем в que
        # дулаем детей
        # добавляем в сет тогда 
        return root

    def __str__(self):
        pass



if __name__== '__main__':
    # sys.argv[1] = path
    path = 'tests/my_case.txt'
    data = utils.parse_file(path)
    solver = Solver(data['puzzle'], data['puzzle_size'])

