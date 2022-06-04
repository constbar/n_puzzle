import sys
import utils
from node import Node
from scipy.spatial import distance


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
    def __init__(self, puzzle):
        # check later if it really all vals needs me
        # yes, i will add __vars everywhere
        self.puzzle = puzzle
        self.p_size = len(puzzle)
        self.aim_puzzle = utils.create_aim_puzzle(self.p_size)

        self.open_list = list()
        self.closed_list = set()

        self.method = [distance.cityblock,
                       distance.euclidean,
                       distance.chebyshev][1]

        self.init_node_cls_variables()
        self.root_node = self.init_root_node()

    def init_node_cls_variables(self):
        Node.matrix_size = self.p_size
        Node.calc_method = self.method
        Node.aim_matrix = self.aim_puzzle
        Node.aim_hash = Node.make_matrix_hash(self.aim_puzzle)

    def init_root_node(self): # rename to like start
        root = Node(self.puzzle, father=None)
        # print(root.level)
        # print(root.__hash__())
        # print(root.aim_hash)
        # print(root.full_cost)
        ch = root.make_children()
        print(ch[2].matrix)
        print('lev', ch[0].level)
        print('cost', ch[0].full_cost)

        print()
        ch2 = ch[2].make_children()[0]
        print(ch2.full_cost)
        exit()

        """
        exit()
        # print(root.__aim_matrix)
        # make = calculation
        # manh
        # self.open_list.append(root)
        # print(root.zero_tile)
        # print(root.h)
        exit()
        # if root.check_node_aim() is True:
        #     return  # make final path to solving
        #
        print(self.open_list[0].matrix)

        # добаляем дитя в новый список только если его нет в сете просмотренных
        # sdelat ocenky nodi
        # добавляем в que
        # дулаем детей
        # добавляем в сет тогда 
        return root
        """

    # надго инициализировать новый ноды и добавить и  в открытый список

    # def __str__(self):
    #     pass



if __name__== '__main__':
    # sys.argv[1] = path
    path = 'tests/my_case.txt'
    data = utils.parse_file(path)
    solver = Solver(data)

