import sys

input = sys.stdin.readline
N, K = map(int, input().split())
MOD = 1000000000
answer = [[0] * (N + 1) for _ in range(K + 1)]
answer[0][0] = 1
for i in range(1, K + 1):
    for j in range(0, N + 1):
        for l in range(0, j + 1):
            answer[i][j] += answer[i - 1][j - l]

print(answer[K][N] % MOD)
