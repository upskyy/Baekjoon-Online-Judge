from collections import deque

N, K = map(int, input().split())
MAX = 100001
check = [False] * MAX
from_ = [0] * MAX
answer = [0] * MAX

q = deque()
q.append(N)
check[N] = True
while q:
    x = q.popleft()
    if (x * 2) < MAX and not check[x * 2]:
        q.append(x * 2)
        check[x * 2] = True
        from_[x * 2] = x
        answer[x * 2] = answer[x] + 1
    if (x + 1) < MAX and not check[x + 1]:
        q.append(x + 1)
        check[x + 1] = True
        from_[x + 1] = x
        answer[x + 1] = answer[x] + 1
    if 0 <= (x - 1) < MAX and not check[x - 1]:
        q.append(x - 1)
        check[x - 1] = True
        from_[x - 1] = x
        answer[x - 1] = answer[x] + 1

print(answer[K])

path = list()
path.append(K)
x = K
while x != N:
    x = from_[x]
    path.append(x)

for _ in range(len(path)):
    top = path.pop()
    print(top, end=' ')

print()
