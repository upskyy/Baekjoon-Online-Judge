from collections import deque

N = int(input())
x1, x2 = map(int, input().split())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
maps = [list() for _ in range(N + 1)]
check = [-1 for _ in range(N + 1)]

for a, b in arr:
    maps[a].append(b)
    maps[b].append(a)

queue = deque()
queue.append(x1)
check[x1] = 0

while queue:
    x = queue.popleft()
    for y in maps[x]:
        if check[y] == -1:
            check[y] = check[x] + 1
            queue.append(y)

print(check[x2])
