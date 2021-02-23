import sys
from collections import deque

input = sys.stdin.readline
N, M, start = map(int, input().split())
a = [[] for _ in range(N + 1)]
check = [False for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(N + 1):
    a[i].sort()


def dfs(x, check):
    check[x] = True
    print(x, end=' ')
    for y in a[x]:
        if not check[y]:
            dfs(y, check)


def bfs(start):
    check = [False for _ in range(N + 1)]
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in a[x]:
            if not check[y]:
                check[y] = True
                q.append(y)


dfs(start, check)
print()
bfs(start)
print()
