import sys

input = sys.stdin.readline
n = int(input())

answer = [[0] * 10 for _ in range(64)]
for i in range(10):
    answer[0][i] = 1
for i in range(1, 64):
    for j in range(10):
        for k in range(j + 1):
            answer[i][j] += answer[i - 1][k]

for _ in range(n):
    print(sum(answer[int(input()) - 1]))
