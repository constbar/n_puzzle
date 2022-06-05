import sys
import utils
from node import Node
from queue import PriorityQueue
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

        self.open_list = PriorityQueue()
        self.closed_list = set()

        self.method = [distance.cityblock,
                       distance.euclidean,
                       distance.chebyshev][0]

        self.init_node_cls_variables()
        self.solution = self.solve_puzzle()

    def init_node_cls_variables(self):
        Node.matrix_size = self.p_size
        Node.calc_method = self.method
        Node.aim_matrix = self.aim_puzzle
        Node.aim_hash = Node.make_matrix_hash(self.aim_puzzle)

    def solve_puzzle(self):
        solution_node = None
        i = 0
        root_node = Node(self.puzzle, father=None)
        if root_node.check_node_aim() is True:
            raise  # !!
        """
        full = []
        ch = root_node.make_children()
        full = full + ch
        # print([i.full_cost for i in full])
        full += full[1].make_children()
        # print([i.level for i in full])
        full += full[-1].make_children()
        # print([i.full_cost for i in full])
        print(full)
        # print(len(full))
        # while not self.open_list.empty()
        for i in full:
            self.open_list.put(i)

        while not self.open_list.empty():
            n = self.open_list.get()
            print(n.full_cost)
            print()
        """

        self.open_list.put(root_node)
        i = 1
        while not self.open_list.empty():
            print('------------------------')
            print('round', i)
            lowest_cost_node = self.open_list.get()
            print()
            print('FULLcost lowest', lowest_cost_node.full_cost, '  and size', self.open_list.qsize())
            print(lowest_cost_node.matrix)
            print()
            children = lowest_cost_node.make_children()
            print([i.full_cost for i in children])
            print('children')
            for k in children:
                print(k.matrix)
                print()
            self.closed_list.add(lowest_cost_node.__hash__())
            # print(self.closed_list)
            for child in children:
                if child.check_node_aim():
                    print('solved')
                    solution_node = child
                    break
                elif child.__hash__() not in self.closed_list:
                    self.open_list.put(child)
            else:
                print('size of closed set', len(self.closed_list))
                print('------------------------')
                i += 1
                continue
            break

        # print(solution_node.matrix)
        self.solution = solution_node.get_solution_path()
        # print(solution)
        for i in self.solution[::-1]:
            # for k in
            print(i)
            print()


if __name__ == '__main__':
    # sys.argv[1] = path
    path = 'tests/my_case.txt'
    data = utils.parse_file(path)
    solver = Solver(data)

