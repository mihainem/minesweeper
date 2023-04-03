from random import randint

class Matrix:
    def __init__(self, rows, cols, val):
        self.rows = rows
        self.cols = cols
        self.matrix = [[val for i in range(cols)] for j in range(rows)]
    
    def __str__(self):
        return "\n".join([str(row) for row in self.matrix])

    def add_mines(self, no_of_mines):
        for i in range(no_of_mines):
            row = randint(0, self.rows - 1)
            col = randint(0, self.cols - 1)
            self.matrix[row][col] = -1
            self.add_mines_counters(row, col)
    
    def add_mines_counters(self, i, j):
        for row in range(i-1, i + 2, 1):
            for col in range(j - 1, j + 2, 1):
                if(row < 0 or row >= self.rows or col < 0 or col >= self.cols):
                    continue

                if self.matrix[row][col] == -1:
                    continue
                self.matrix[row][col] = max(self.matrix[row][col], self.count_mines(row, col))

    def count_mines(self, i, j):
        count = 0
        for row in range(i-1,i+2, 1):
            for col in range(j-1,j+2, 1):
                if(row < 0 or row >= self.rows or col < 0 or col >= self.cols):
                    continue
                if self.matrix[row][col] == -1:
                    count += 1
        return count
    
    def add_mines_for_level(self, level):
        no_of_mines = self.rows * self.cols // max(abs((4 - min(level, 4)) % 5), 1)
        self.add_mines(no_of_mines)

