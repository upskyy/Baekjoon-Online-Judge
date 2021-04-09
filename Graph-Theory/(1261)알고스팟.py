from collections import deque

M, N = map(int, input().split())
maps = [[int(i) for i in input()] for _ in range(N)]
check = [[-1] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
  
q = deque()
q.append((0, 0))
check[0][0] = 0

while q:
    x, y = q.popleft()

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < M and check[new_x][new_y] == -1:
            if maps[new_x][new_y] == 1:
                check[new_x][new_y] = (check[x][y] + 1)
                q.append((new_x, new_y))
            else:
                check[new_x][new_y] = check[x][y]
                q.appendleft((new_x, new_y))

print(check[N - 1][M - 1])


# 메모리 초과
from collections import deque

M, N = map(int, input().split())
maps = [[int(i) for i in input()] for _ in range(N)]
check = [[-1] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
q.append((0, 0))
check[0][0] = 0

while q:
    x, y = q.popleft()

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < N and 0 <= new_y < M:
            if check[new_x][new_y] == -1 or check[new_x][new_y] > check[x][y]:
                if maps[new_x][new_y] == 1:
                    check[new_x][new_y] = (check[x][y] + 1)
                    q.append((new_x, new_y))
                else:
                    check[new_x][new_y] = check[x][y]
                    q.append((new_x, new_y))
                    
print(check[N - 1][M - 1])
