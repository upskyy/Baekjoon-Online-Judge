import sys

N, M = map(int, input().split())
board = [input() for _ in range(N)]
check = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def calculate(x, y, px, py, color):
    if check[x][y]:
        return True
    check[x][y] = True
    for k in range(4):
        new_x, new_y = x + dx[k], y + dy[k]
        if 0 <= new_x < N and 0 <= new_y < M:
            if not (new_x == px and new_y == py) and board[new_x][new_y] == color:
                if calculate(new_x, new_y, x, y, color):
                    return True

    return False


for i in range(N):
    for j in range(M):
        if check[i][j]:
            continue
        if calculate(i, j, 0, 0, board[i][j]):
            print('Yes')
            sys.exit()

print('No')
