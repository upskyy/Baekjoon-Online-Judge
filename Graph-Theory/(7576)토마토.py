from collections import deque
import sys

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
arr = list()
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
flag = False
count = 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            flag = True
            arr.append((i, j, 0))

if not flag:
    print(-1)
    sys.exit()

queue = deque()
for position in arr:
    queue.append(position)

while queue:
    x, y, count = queue.popleft()
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < M:
            if maps[new_x][new_y] == 0:
                maps[new_x][new_y] = 1
                queue.append((new_x, new_y, count + 1))

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            flag = False

if flag:
    print(count)
else:
    print(-1)
