from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    answer[x][y] = cnt

    while q:
        x, y = q.popleft()
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < H and 0 <= new_y < W and maps[new_x][new_y] == 1 and answer[new_x][new_y] == 0:
                answer[new_x][new_y] = cnt
                q.append((new_x, new_y))


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    else:
        maps = [list(map(int, input().split())) for _ in range(H)]
        answer = [[0] * W for _ in range(H)]
        cnt = 0

        for i in range(H):
            for j in range(W):
                if maps[i][j] == 1 and answer[i][j] == 0:
                    cnt += 1
                    bfs(i, j, cnt)

        print(cnt)
