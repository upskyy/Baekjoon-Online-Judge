from collections import deque

N, M = map(int, input().split())
reference = [0 for _ in range(N + 1)]
maps = [list() for _ in range(N + 1)]
queue = deque()

arr = [list(map(int, input().split())) for _ in range(M)]

for x1, x2 in arr:
    maps[x1].append(x2)
    reference[x2] += 1

for i in range(1, N + 1):
    if reference[i] == 0:
        queue.append(i)

while queue:
    x = queue.popleft()
    for y in maps[x]:
        reference[y] -= 1
        if reference[y] == 0:
            queue.append(y)
    print(x, end=' ')
