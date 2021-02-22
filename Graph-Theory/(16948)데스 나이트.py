from collections import deque
import sys

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
check = [[-1] * N for _ in range(N)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

q = deque()
q.append((r1, c1))
check[r1][c1] = 0

while q:
    x, y = q.popleft()
    for i in range(6):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < N and check[new_x][new_y] == -1:
            check[new_x][new_y] = check[x][y] + 1
            q.append((new_x, new_y))
            if new_x == r2 and new_y == c2:
                print(check[new_x][new_y])
                sys.exit()

print(-1)


