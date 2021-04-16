N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]


def go(x, y, dx, dy):
    k = 1
    for _ in range(N - 1):
        nx, ny = x + dx, y + dy
        diff = maps[nx][ny] - maps[x][y]

        if abs(diff) > 1:
            return 0
        if diff == 1:
            if k >= L:
                k = 0
            else:
                return 0
        if diff == -1:
            if k >= 0:
                k = -L
            else:
                return 0
        k += 1
        x, y = nx, ny

    return 1 if k >= 0 else 0


answer = 0
for i in range(N):
    answer += go(0, i, 1, 0)
    answer += go(i, 0, 0, 1)

print(answer)