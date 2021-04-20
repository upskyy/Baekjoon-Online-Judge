from collections import deque


def bfs(x, y):
    visited = set([(x, y)])
    q = deque([(x, y)])

    total, num = 0, 0
    while q:
        x, y = q.popleft()

        total += maps[x][y]
        num += 1

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and (nx, ny) not in total_visited:
                diff = abs(maps[x][y] - maps[nx][ny])
                if l <= diff <= r:
                    global is_move
                    is_move = True

                    q.append((nx, ny))
                    visited.add((nx, ny))

    return total // num, visited


n, l, r = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    total_visited = set()
    is_move = False
    unions = list()

    for i in range(n):
        for j in range(n):
            if (i, j) not in total_visited:
                changed_num, visited = bfs(i, j)
                unions.append((changed_num, visited))
                total_visited |= visited

    for (changed_num, union) in unions:
        for x, y in union:
            maps[x][y] = changed_num

    if not is_move:
        break

    answer += 1

print(answer)
