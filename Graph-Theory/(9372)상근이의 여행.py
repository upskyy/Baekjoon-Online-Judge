from collections import deque


def bfs():
    count = 0
    q = deque()
    q.append(1)
    check[1] = True

    while q:
        x = q.popleft()
        for i in maps[x]:
            if not check[i]:
                count += 1
                check[i] = True
                q.append(i)

    print(count)


T = int(input())

for _ in range(T):
    check = [False for _ in range(1001)]
    N, M = map(int, input().split())
    maps = dict()
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

    bfs()
