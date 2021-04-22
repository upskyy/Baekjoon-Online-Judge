r, c, t = map(int, input().split())
air_fresh = list()
maps = [list(map(int, input().split())) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dust_move():
    temp = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if maps[x][y] >= 5:
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != -1:
                        cnt += 1
                        temp[nx][ny] += maps[x][y] // 5
                if cnt:
                    temp[x][y] -= (maps[x][y] // 5) * cnt

    for i in range(r):
        for j in range(c):
            maps[i][j] += temp[i][j]


def air_move():
    temp = [[-2] * c for _ in range(r)]
    up_machine = 0
    for row in range(r):
        if maps[row][0] == -1:
            up_machine = row
            break

    for i in range(1, c):
        temp[0][i - 1] = maps[0][i]
        temp[up_machine][i] = maps[up_machine][i - 1]
        temp[up_machine][1] = 0

    for i in range(1, up_machine + 1):
        if maps[i][0] != -1:
            temp[i][0] = maps[i - 1][0]
        temp[i - 1][c - 1] = maps[i][c - 1]

    for i in range(1, c):
        temp[r - 1][i - 1] = maps[r - 1][i]
        temp[up_machine + 1][i] = maps[up_machine + 1][i - 1]
        temp[up_machine + 1][1] = 0

    for i in range(up_machine + 2, r):
        if maps[i - 1][0] != -1:
            temp[i - 1][0] = maps[i][0]
        temp[i][c - 1] = maps[i - 1][c - 1]

    for i in range(r):
        for j in range(c):
            if temp[i][j] != -2:
                maps[i][j] = temp[i][j]


time = 0
for _ in range(t):
    dust_move()
    air_move()
    time += 1

answer = 0
for i in range(r):
    for j in range(c):
        if maps[i][j] > 0:
            answer += maps[i][j]
print(answer)