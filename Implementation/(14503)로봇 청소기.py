N, M = map(int, input().split())
x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean(x, y, d):
    global answer
    if maps[x][y] == 0:
        maps[x][y] = 2
        answer += 1

    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if maps[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd

    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if maps[nx][ny] == 1:
        return
    else:
        clean(nx, ny, d)


clean(x, y, d)
print(answer)




