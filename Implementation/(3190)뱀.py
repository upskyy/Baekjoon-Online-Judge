from collections import deque

N = int(input())
K = int(input())
check = [[0] * N for _ in range(N)]  # 공백은 0, 뱀은 1
for _ in range(K):
    x, y = map(int, input().split())
    check[x - 1][y - 1] = 2  # 사과는 2

L = int(input())
pos = [input().split() for _ in range(L)]
check[0][0] = 1
ans = 0

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]
x, y, k = 0, 0, 1
visited = deque([[x, y]])

while True:
    ans += 1
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < N and 0 <= ny < N and check[nx][ny] != 1:
        if check[nx][ny] == 0:
            tx, ty = visited.popleft()
            check[tx][ty] = 0
        check[nx][ny] = 1
        visited.append([nx, ny])

        if pos and ans == int(pos[0][0]):
            if pos[0][1] == 'D':
                k = (k + 1) % 4
            elif pos[0][1] == 'L':
                k = (k + 3) % 4
            del pos[0]

        x, y = nx, ny

    else:
        print(ans)
        exit()