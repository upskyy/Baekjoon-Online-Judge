import sys

input = sys.stdin.readline
num = int(input())
ans = [0 for _ in range(num + 1)]
for i in range(2, num + 1):
    ans[i] = ans[i - 1] + 1
    if (i % 2 == 0) and (ans[i] > ans[i // 2] + 1):
        ans[i] = ans[i // 2] + 1
    if (i % 3 == 0) and (ans[i] > ans[i // 3] + 1):
        ans[i] = ans[i // 3] + 1

print(ans[num])

