import sys

input = sys.stdin.readline

num = int(input())
ans = [0] * 1000
for i in range(num):
    if i == 0:
        ans[i] = 1
    elif i == 1:
        ans[i] = 2
    else:
        ans[i] = ans[i - 1] + ans[i - 2]

print(ans[num - 1] % 10007)
