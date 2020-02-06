class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def find_possibilities(self, row_number, column_number):
        possibilities = set(range(1, 10))
        
        row = self.puzzle[row_number]
        column = [row[column_number] for row in self.puzzle]
        box = self.get_box(row_number, column_number)
        
        for item in row + column + box:
            if not isinstance(item, list)and item in possibilities:
                possibilities.remove(item)
        return possibilities

    def get_box(self, row_number, column_number):
        start_y = column_number // 3 * 3
        start_x = row_number // 3 * 3
        
        if start_x < 0:
            start_x = 0
        if start_y < 0:
            start_y = 0
            
        box = []
        
        for i in range(start_x, 3 + start_x):
            box.extend(self.puzzle[i][start_y:start_y + 3])
            
        return box

    def find_spot(self):
        unsolved = True
        
        while unsolved:
            unsolved = False
            
            for row_number, row in enumerate(self.puzzle):
                for column_number, item in enumerate(row):
                    if item == 0:
                        unsolved = True
                        
                        possibilities = self.find_possibilities(row_number, column_number)
                        if len(possibilities) == 1:
                            self.puzzle[row_number][column_number] = list(possibilities)[0]
        return self.puzzle

def sudoku(puzzle):
    sudoku = SudokuSolver(puzzle)
    return sudoku.find_spot()