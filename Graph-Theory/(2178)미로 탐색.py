from collections import deque

N, M = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(N)]
answer = [[0] * M for _ in range(N)]
check = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0))
check[0][0] = True
answer[0][0] = 1
while q:
    x, y = q.popleft()
    for k in range(4):
        new_x, new_y = x + dx[k], y + dy[k]
        if 0 <= new_x < N and 0 <= new_y < M:
            if not check[new_x][new_y] and a[x][y] == 1:
                q.append((new_x, new_y))
                answer[new_x][new_y] = answer[x][y] + 1
                check[new_x][new_y] = True

print(answer[N - 1][M - 1])
