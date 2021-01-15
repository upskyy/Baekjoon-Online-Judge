from collections import deque

S = int(input())
MAX = 1001
check = [[False] * MAX for _ in range(MAX)]
answer = [[0] * MAX for _ in range(MAX)]

q = deque()
q.append((1, 0))
check[1][0] = True
while q:
    s, c = q.popleft()
    if s < MAX and not check[s][s]:
        q.append((s, s))
        check[s][s] = True
        answer[s][s] = answer[s][c] + 1
    if (s + c) < MAX and not check[s + c][c]:
        q.append((s + c, c))
        check[s + c][c] = True
        answer[s + c][c] = answer[s][c] + 1
    if (s - 1) >= 0 and not check[s - 1][c]:
        q.append((s - 1, c))
        check[s - 1][c] = True
        answer[s - 1][c] = answer[s][c] + 1

ans = -1
for i in range(MAX):
    if answer[S][i] != 0:
        if ans == -1 or ans > answer[S][i]:
            ans = answer[S][i]

print(ans)

