from collections import deque

N = int(input())

maps = [list(map(str, input())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    color = 0

    if maps[x][y] == 'R':
        color = 1
    elif maps[x][y] == 'G':
        color = 2
    elif maps[x][y] == 'B':
        color = 3

    region[x][y] = color
    while q:
        x, y = q.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                if region[new_x][new_y] == 0:
                    if color == 1:
                        if maps[new_x][new_y] == 'R':
                            region[new_x][new_y] = color
                            q.append((new_x, new_y))
                    elif color == 2:
                        if maps[new_x][new_y] == 'G':
                            region[new_x][new_y] = color
                            q.append((new_x, new_y))
                    elif color == 3:
                        if maps[new_x][new_y] == 'B':
                            region[new_x][new_y] = color
                            q.append((new_x, new_y))


region = [[0] * N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        if region[i][j] == 0:
            answer += 1
            bfs(i, j)

print(answer, end=' ')

for i in range(N):
    for j in range(N):
        if maps[i][j] == 'G':
            maps[i][j] = 'R'


region = [[0] * N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        if region[i][j] == 0:
            answer += 1
            bfs(i, j)

print(answer)

