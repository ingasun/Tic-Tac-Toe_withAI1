import random


class TicTacToe:
    def __init__(self):
        # self.board = []
        self.board = [[' ', ' ', ' '],  # (1, 3) (2, 3) (3, 3)
                      [' ', ' ', ' '],  # (1, 2) (2, 2) (3, 2)
                      [' ', ' ', ' ']]  # (1, 1) (2, 1) (3, 1)
        self.state = 'Game not finished'

    def start(self):
        #  self.get_initial_board()
        self.print_empty_field()
        #  self.print_board()
        self.get_move()
        self.game_state()

    def print_empty_board(self):
        """Output the 3x3 field with cells"""
        print('---------')
        for i in range(3):
            out = '| '
            for j in range(3):
                out += self.board[i][j] + ' '
            out += '|'
            print(out)
        print('---------')

    def get_ai_coord_for_easy(self):
        """Get coordinates for AI move for easy level"""
        # get the list of coordinates of empty cells
        empty_cells = [[row, col] for row in range(len(self.board))
                       for col in range(len(self.board[row]))
                       if self.board[row][col] == ' ']
        # take the coordinates of a random empty cell
        self.coord = random.choice(empty_cells)

    def get_initial_board(self):
        cells = list(input("Enter cells: "))
        c = [' ' if x == '_' else x for x in cells]
        self.board=[[c[0], c[1], c[2]],
                     [c[3], c[4], c[5]],
                     [c[6], c[7], c[8]]]

    def print_board(self):
        print('---------')
        print(f'| {self.board[0][0]} {self.board[0][1]} {self.board[0][2]} |')
        print(f'| {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} |')
        print(f'| {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} |')
        print('---------')

    def get_move(self):
        while True:
            coords = input('Enter the coordinates: ')
            if len(coords.split()) < 2:
                print('You should enter numbers!')
                continue
            a, b = coords.split()
            if a.isdigit() and b.isdigit():
                a, b = int(a), int(b)
                if not (1 <= a <= 3) or not (1 <= b <= 3):
                    print('Coordinates should be from 1 to 3!')
                    continue
                else:
                    i, j = self.transpose_coordinates(a, b)
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.next_move()
                        self.print_board()
                        break
                    else:
                        print('This cell is occupied! Choose another one!')
                        continue
            else:
                print('You should enter numbers!')
                continue

    def game_state(self):
        if (self.count_char('X') + self.count_char('O') >= 9):
            self.state = 'Draw'
        self.check_win()
        print(self.state)

    def transpose_coordinates(self, x, y):
        return 3 - y, x - 1

    def count_char(self, c):
        return self.board[0].count(c) + self.board[1].count(c) + self.board[2].count(c)

    def next_move(self):
        return 'O' if self.count_char('X') > self.count_char('O' )else 'X'

    def check_row(self, row):
        if all(i == 'X' for i in row):
            self.state = 'X wins'
        elif all(i == 'O' for i in row):
            self.state = 'O wins'

    def check_win(self):
        b = self.board
        c = [[self.board[i][j] for j in range(3)] for i in range(3)]
        for row in [b[0], b[1] ,b[2], c[0], c[1], c[2],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]]]:
            self.check_row(row)


if __name__ == "__main__":
    game = TicTacToe()
    #  game.start()
    game.print_empty_board()
    game.get_move()