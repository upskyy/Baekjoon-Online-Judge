import sys

input = sys.stdin.readline

num = int(input())
for _ in range(num):
    n = int(input())
    ans = [0] * 10
    for i in range(n):
        if i == 0:
            ans[i] = 1
        elif i == 1:
            ans[i] = 2
        elif i == 2:
            ans[i] = 4
        else:
            ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]
    print(ans[n-1])
