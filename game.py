from matrix import Matrix


class Game:

    def __init__(self):
        rows = int(input("How many rows?: "))
        cols = int(input("How many columns?: "))
        level = int(input("""Pick your experience level:
0-Begginer
1-Intermediate 
2-Advanced 
3-Expert 
4-Insane:"""))
        self.front_matrix = Matrix(rows, cols, "_")
        self.back_matrix = Matrix(rows, cols, 0)
        self.back_matrix.add_mines_for_level(level)
        self.game_over = False
        self.play()

    def __str__(self):
        return str(self.front_matrix)

    def play(self):
        while not self.game_over:
            #Uncomment this line to debug back_matrix
            #print(str(self.back_matrix))
            print(self)
            line = input("Enter pairs for rows and cols (e.g. 1 2): ")
            action = input("Enter action (o - open, f - flag): ")
            splits = line.split()
            rows_and_cols = []
            count_numbers = len(splits)
            for i in range(0, count_numbers - (count_numbers % 2), 2):
                rows_and_cols.append((int(splits[i]), int(splits[i + 1])))
            self.set_multiple(rows_and_cols, action)

        retry = input("Do you want to retry? (y/n): ")
        if retry == "y":
            self.__init__()

    def set_multiple(self, list, action):
        for row, col in list:
            if action == "o":
                self.open_cell(row, col)
            elif action == "f":
                self.set_flag(row, col)
            else:
                print("Invalid action!")

    def set_flag(self, row, col):
        self.front_matrix.matrix[row][col] = "F"

    def open_cell(self, row, col):
        if self.back_matrix.matrix[row][col] == -1:
            self.game_over = True
            print("You lost")
        else:
            self.front_matrix.matrix[row][col] = self.back_matrix.matrix[row][col]
            self.check_if_won()

    def check_if_won(self):
        for row in range(self.front_matrix.rows):
            for col in range(self.front_matrix.cols):
                if self.front_matrix.matrix[row][col] == "_" \
                    or self.front_matrix.matrix[row][col] == "F" \
                        and self.back_matrix.matrix[row][col] != -1:
                    return
        self.game_over = True
        print("You won!")


print("Welcome to minesweeper. Let's setup the game")


game1 = Game()
