import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
width, height = 300, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("테트리스")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 격자 크기 설정
grid_size = 30
grid_width = width // grid_size
grid_height = height // grid_size

# 테트리스 블록 정의
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# 블록 색상 정의
colors = [
    RED,
    GREEN,
    BLUE,
    (255, 165, 0),
    (128, 0, 128),
    (0, 191, 255),
    (255, 140, 0)
]

# 게임 보드 초기화
board = [[BLACK] * grid_width for _ in range(grid_height)]

# 블록 클래스 정의
class Block:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(colors)

    def draw(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, ((self.x + j) * grid_size, (self.y + i) * grid_size,
grid_size, grid_size))
                    pygame.draw.rect(screen, BLACK, ((self.x + j) * grid_size, (self.y + i) * grid_size,
grid_size, grid_size), 1)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

# 블록 충돌 확인 함수
def check_collision(block):
    for i, row in enumerate(block.shape):
        for j, cell in enumerate(row):
            if cell:
                if block.x + j < 0 or block.x + j >= grid_width or block.y + i >= grid_height or board[block.y +
i][block.x + j] != BLACK:
                    return True
    return False

# 줄 지우기 함수
def clear_lines():
    global board
    new_board = [row for row in board if any(cell == BLACK for cell in row)]
    lines_cleared = grid_height - len(new_board)
    board = [[BLACK] * grid_width for _ in range(lines_cleared)] + new_board

# 메인 루프
def main():
    clock = pygame.time.Clock()
    current_block = Block(grid_width // 2, 0, random.choice(shapes))
    game_over = False

    while not game_over:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(Block(current_block.x - 1, current_block.y,
current_block.shape)):
                    current_block.move(-1, 0)
                elif event.key == pygame.K_RIGHT and not check_collision(Block(current_block.x + 1,
current_block.y, current_block.shape)):
                    current_block.move(1, 0)
                elif event.key == pygame.K_DOWN and not check_collision(Block(current_block.x, current_block.y +
1, current_block.shape)):
                    current_block.move(0, 1)
                elif event.key == pygame.K_UP:
                    rotated_block = Block(current_block.x, current_block.y,
list(zip(*reversed(current_block.shape))))
                    if not check_collision(rotated_block):
                        current_block.rotate()

        # 블록 하강
        new_block = Block(current_block.x, current_block.y + 1, current_block.shape)
        if not check_collision(new_block):
            current_block.move(0, 1)
        else:
            for i, row in enumerate(current_block.shape):
                for j, cell in enumerate(row):
                    if cell:
                        board[current_block.y + i][current_block.x + j] = current_block.color
            clear_lines()
            current_block = Block(grid_width // 2, 0, random.choice(shapes))
            if check_collision(current_block):
                game_over = True

        # 게임 보드 그리기
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                pygame.draw.rect(screen, cell, (x * grid_size, y * grid_size, grid_size, grid_size))
                pygame.draw.rect(screen, BLACK, (x * grid_size, y * grid_size, grid_size, grid_size), 1)

        # 현재 블록 그리기
        current_block.draw()

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()