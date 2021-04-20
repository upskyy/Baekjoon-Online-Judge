import copy

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cctv = list()
for i in range(n):
    for j in range(m):
        if maps[i][j] not in (0, 6):
            cctv.append([maps[i][j], i, j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
di = [0, [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[1, 2], [1, 3], [0, 2], [0, 3]], [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],[[0, 1, 2, 3]]]
min_value = float('inf')


def dfs(start, maps):
    global min_value
    if start == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 0:
                    cnt += 1
        min_value = min(min_value, cnt)
        return

    num, x, y = cctv[start]
    for dir in di[num]:
        tmp = copy.deepcopy(maps)
        for k in dir:
            nx, ny = x + dx[k], y + dy[k]
            while 0 <= nx < n and 0 <= ny < m:
                if tmp[nx][ny] == 6:
                    break
                elif tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'

                nx += dx[k]
                ny += dy[k]
        dfs(start + 1, tmp)


dfs(0, maps)
print(min_value)