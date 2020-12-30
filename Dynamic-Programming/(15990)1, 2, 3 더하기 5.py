import sys

input = sys.stdin.readline
MOD = 1000000009
MAX = 100000
ans = [[0, 0, 0] for _ in range(MAX)]
for i in range(MAX):
    if i == 0:
        ans[i][0] = 1
    elif i == 1:
        ans[i][0] = ans[i - 1][1] + ans[i - 1][2]
        ans[i][1] = 1
    elif i == 2:
        ans[i][0] = ans[i - 1][1] + ans[i - 1][2]
        ans[i][1] = ans[i - 2][0] + ans[i - 2][2]
        ans[i][2] = 1
    else:
        ans[i][0] = ans[i - 1][1] + ans[i - 1][2]
        ans[i][1] = ans[i - 2][0] + ans[i - 2][2]
        ans[i][2] = ans[i - 3][0] + ans[i - 3][1]
    ans[i][0] %= MOD
    ans[i][1] %= MOD
    ans[i][2] %= MOD

num = int(input())
for _ in range(num):
    n = int(input())
    print(sum(ans[n - 1]) % MOD)
