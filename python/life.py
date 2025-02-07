import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 게임 보드 크기 설정
BOARD_SIZE = 100

# 초기 상태 설정 (랜덤)
def initialize_board(size):
    return np.random.choice([0, 1], size=(size, size), p=[0.7, 0.3])

# 다음 세대 계산
def next_generation(board):
    new_board = np.zeros_like(board)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            # 주변 8개 셀의 상태를 확인
            neighbors = board[max(0, i-1):min(i+2, board.shape[0]), max(0, j-1):min(j+2, board.shape[1])]
            total = np.sum(neighbors) - board[i, j]  # 현재 셀은 제외
            # 규칙 적용
            if board[i, j] == 1:
                if total < 2 or total > 3:
                    new_board[i, j] = 0  # 죽음
                else:
                    new_board[i, j] = 1  # 생존
            else:
                if total == 3:
                    new_board[i, j] = 1  # 탄생
    return new_board

# 애니메이션 업데이트 함수
def update(frame, img, board):
    new_board = next_generation(board)
    img.set_data(new_board)
    board[:] = new_board[:]
    return img

# 메인 함수
def main():
    board = initialize_board(BOARD_SIZE)
    fig, ax = plt.subplots()
    img = ax.imshow(board, cmap='binary', interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, board), frames=100, interval=50, save_count=50)
    plt.show()

if __name__ == "__main__":
    main()
