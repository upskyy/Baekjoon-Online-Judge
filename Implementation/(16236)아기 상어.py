from collections import deque

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]


def bfs(x, y):
    q, visited = deque([(x, y)]), [(x, y)]
    time = 0
    shark = 2
    eat = 0
    eat_flag = False
    answer = 0

    while q:
        size = len(q)

        q = deque(sorted(q))
        for _ in range(size):
            x, y = q.popleft()

            if board[x][y] != 0 and board[x][y] < shark:
                board[x][y] = 0
                eat += 1

                if eat == shark:
                    shark += 1
                    eat = 0

                q, visited = deque(), [(x, y)]
                eat_flag = True

                answer = time

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    if board[nx][ny] <= shark:
                        q.append((nx, ny))
                        visited.append((nx, ny))

            if eat_flag:
                eat_flag = False
                break

        time += 1
    return answer


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            print(bfs(i, j))
            exit()