from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

 
def bfs(x, y, count):
    queue = deque()
    queue.append((x, y))
    check[x][y] = count
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if 0 <= new_x < N and 0 <= new_y < M:
                if check[new_x][new_y] == 0 and maps[new_x][new_y] == 1:
                    check[new_x][new_y] = count
                    queue.append((new_x, new_y))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    maps = [[0] * M for _ in range(N)]
    check = [[0] * M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        maps[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if check[i][j] == 0 and maps[i][j] == 1:
                cnt += 1
                bfs(i, j, cnt)

    print(cnt)



