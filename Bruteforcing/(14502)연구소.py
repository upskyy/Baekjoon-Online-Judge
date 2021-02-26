from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
max_value = 0


def bfs():
    global max_value
    result = 0
    temp = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            temp[i][j] = maps[i][j]

    q = deque()
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if 0 <= new_x < N and 0 <= new_y < M:
                if temp[new_x][new_y] == 0:
                    temp[new_x][new_y] = 2
                    q.append((new_x, new_y))

    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                result += 1

    max_value = max(max_value, result)


def set_block(count):
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                set_block(count + 1)
                maps[i][j] = 0


set_block(0)
print(max_value)
