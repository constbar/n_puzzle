
def create_random_puzzle(puzzle_size):
	rand = list(range(size**2))
	random.shuffle(rand)
	rand = np.array(rand).reshape(size, size)
	return rand
# kek = create_random_puzzle(size)
# print(kek)


def create_aim_puzzle(puzzle_size):
	"""
	for snake/ulitka location
	"""
	deq = collections.deque(range(1, size**2))
	res = np.zeros((size, size), dtype=int)

	turn_flag = 0
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









import numpy as np
from scipy.spatial import distance # type: ignore



def manhattan_distance(matrix1: np.ndarray, matrix2: np.ndarray): # -> int
	l = len(matrix1) # remake in size
	return sum([distance.cityblock(np.where(matrix1 == i),
		np.where(matrix2 == i)) for i in range(1, l**2)])

def euclidean_distance(matrix1, matrix2): # float
	l = len(matrix1)
	return sum([distance.euclidean(np.where(matrix1 == i),
		np.where(matrix2 == i)) for i in range(1, l**2)])

def chebyshev_distance(matrix1, matrix2): # int or float
	l = len(matrix1)
	return sum([distance.chebyshev(np.where(matrix1 == i),
		np.where(matrix2 == i)) for i in range(1, l**2)])