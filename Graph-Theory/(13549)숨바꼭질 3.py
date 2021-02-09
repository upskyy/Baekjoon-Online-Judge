from collections import deque
import sys

N, K = map(int, input().split())
MAX = 100000
check = [-1 for _ in range(MAX + 1)]
dx = [2, -1, 1]
q = deque()
q.append(N)
check[N] = 0

while q:
    x = q.popleft()

    for i in range(3):
        if i == 0:
            new_x = x * dx[i]
            if 0 <= new_x <= MAX and check[new_x] == -1 and abs(x - K) > abs(new_x - K):
                check[new_x] = check[x]
                q.appendleft(new_x)
        else:
            new_x = x + dx[i]
            if 0 <= new_x <= MAX and check[new_x] == -1:
                check[new_x] = check[x] + 1
                q.append(new_x)

        if new_x == K:
            print(check[new_x])
            sys.exit()

