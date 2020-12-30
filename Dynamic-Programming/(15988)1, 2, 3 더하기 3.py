import sys

input = sys.stdin.readline
MOD = 1000000009
MAX = 1000000
ans = [0 for _ in range(MAX)]
for i in range(MAX):
    if i == 0:
        ans[i] = 1
    elif i == 1:
        ans[i] = 2
    elif i == 2:
        ans[i] = 4
    else:
        ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]
    ans[i] %= MOD

num = int(input())
for _ in range(num):
    n = int(input())
    print(ans[n - 1])
