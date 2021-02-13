from collections import deque

N, M = map(int, input().split())
maps = dict()
check = [False for _ in range(1001)]
count = 0


def bfs(x):
    q = deque()
    q.append(x)
    check[x] = True

    while q:
        x = q.popleft()
        if x in maps.keys():
            for i in maps[x]:
                if not check[i]:
                    check[i] = True
                    q.append(i)


for _ in range(M):
    x1, x2 = map(int, input().split())
    if x1 in maps.keys():
        maps[x1].append(x2)
    else:
        maps[x1] = list()
        maps[x1].append(x2)

    if x2 in maps.keys():
        maps[x2].append(x1)
    else:
        maps[x2] = list()
        maps[x2].append(x1)

for i in range(1, N + 1):
    if not check[i]:
        count += 1
        bfs(i)

print(count)
