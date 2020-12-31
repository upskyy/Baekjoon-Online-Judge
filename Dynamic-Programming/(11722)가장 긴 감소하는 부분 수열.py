import sys

input = sys.stdin.readline
num = int(input())
sequence = list(map(int, input().split()))
sequence = sequence[::-1]
ans = [1 for _ in range(num)]
for i in range(num):
    for j in range(i):
        if (sequence[j] < sequence[i]) and (ans[i] < ans[j] + 1):
            ans[i] = ans[j] + 1
print(max(ans))
