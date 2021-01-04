import sys

input = sys.stdin.readline
length = int(input())
answer = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(length + 1)]
MOD = 1000000000
for i in range(1, length + 1):
    if i == 1:
        for k in range(1, 10):
            answer[i][k] = 1
        continue
    for j in range(10):
        if j == 0:
            answer[i][j] = answer[i - 1][j + 1]
        elif j == 9:
            answer[i][j] = answer[i - 1][j - 1]
        else:
            answer[i][j] = answer[i - 1][j - 1] + answer[i - 1][j + 1]
print(sum(answer[length]) % MOD)
