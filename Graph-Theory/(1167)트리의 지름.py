from collections import deque


def bfs(x, mode):
    q = deque()
    q.append(x)
    c = [-1 for _ in range(n + 1)]
    c[x] = 0
    while q:
        x = q.popleft()
        for nx, w in maps[x]:
            if c[nx] == -1:  # 방문 했는지 확인
                c[nx] = c[x] + w
                q.append(nx)
    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)


n = int(input())
maps = [[] for _ in range(n + 1)]

for _ in range(n):
    info = list(map(int, input().split()))
    for i in range((len(info) // 2) - 1):
        maps[info[0]].append([info[2 * i + 1], info[2 * i + 2]])
        maps[info[2 * i + 1]].append([info[0], info[2 * i + 2]])

print(bfs(bfs(1, 1), 2))
