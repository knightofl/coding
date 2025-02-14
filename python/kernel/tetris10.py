import curses
import random

class TetrisGame:
    SHAPES = [
        [[1, 1, 1, 1]],  # I shape
        [[1, 1], [1, 1]],  # O shape
        [[0, 1, 0], [1, 1, 1]],  # T shape
        [[0, 0, 1], [1, 1, 1]],  # L shape
        [[1, 0, 0], [1, 1, 1]],  # J shape
        [[1, 1, 0], [0, 1, 1]],  # S shape
        [[0, 1, 1], [1, 1, 0]]   # Z shape
    ]

    COLORS = ['$', '#', '@', '%', '&', '*', '+']

    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.current_shape = None
        self.current_color = None
        self.current_x = 0
        self.current_y = 0

    def new_block(self):
        self.current_shape = random.choice(self.SHAPES)
        self.current_color = random.choice(self.COLORS)
        self.current_x = (self.width - len(self.current_shape[0])) // 2
        self.current_y = 0

    def rotate_shape(self, shape):
        return [list(reversed(col)) for col in zip(*shape)]

    def collide(self, x, y, shape):
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    ny = y + i
                    nx = x + j
                    if ny >= self.height or nx < 0 or nx >= self.width or self.board[ny][nx] != ' ':
                        return True
        return False

    def fix_block(self):
        shape = self.current_shape
        color = self.current_color
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    ny = self.current_y + i
                    nx = self.current_x + j
                    self.board[ny][nx] = color
        self.clear_lines()
        self.new_block()
        if self.collide(self.current_x, self.current_y, shape):
            self.game_over = True

    def clear_lines(self):
        new_board = [row for row in self.board if ' ' in row]
        lines_cleared = self.height - len(new_board)
        for _ in range(lines_cleared):
            new_board.insert(0, [' ' for _ in range(self.width)])
        self.board = new_board

    def draw(self, stdscr):
        stdscr.clear()
        for y, row in enumerate(self.board):
            stdscr.addstr(y, 0, ''.join(row))
        shape = self.current_shape
        color = self.current_color
        if shape:
            for i, row in enumerate(shape):
                for j, cell in enumerate(row):
                    if cell:
                        ny = self.current_y + i
                        nx = self.current_x + j
                        stdscr.addch(ny, nx, color)
        stdscr.refresh()

    def game_loop(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(500)  # Adjust the speed here

        self.game_over = False
        self.new_block()

        while not self.game_over:
            self.draw(stdscr)
            key = stdscr.getch()
            if key == ord('q'):
                break
            elif key == curses.KEY_UP:
                rotated_shape = self.rotate_shape(self.current_shape)
                if not self.collide(self.current_x, self.current_y, rotated_shape):
                    self.current_shape = rotated_shape
            elif key == curses.KEY_DOWN:
                if not self.collide(self.current_x, self.current_y + 1, self.current_shape):
                    self.current_y += 1
                else:
                    self.fix_block()
            elif key == curses.KEY_LEFT:
                if not self.collide(self.current_x - 1, self.current_y, self.current_shape):
                    self.current_x -= 1
            elif key == curses.KEY_RIGHT:
                if not self.collide(self.current_x + 1, self.current_y, self.current_shape):
                    self.current_x += 1

            # Automatic downward movement
            if not self.collide(self.current_x, self.current_y + 1, self.current_shape):
                self.current_y += 1
            else:
                self.fix_block()

        stdscr.addstr(self.height // 2, (self.width - len("Game Over")) // 2, "Game Over")
        stdscr.refresh()
        stdscr.getch()

def main(stdscr):
    game = TetrisGame()
    game.game_loop(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)