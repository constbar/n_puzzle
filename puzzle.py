class Puzzle:
    def __init__(self, puzzle, puzzle_size):
        self.puzzle = puzzle
        self.puzzle_size = puzzle_size

    def __str__(self):
        for i in range(0, self.puzzle_size**2, self.puzzle_size):
            print(self.puzzle[i: i + self.puzzle_size])