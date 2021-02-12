N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * i for i in range(1, N + 1)]

for i in range(N):
    if i == 0:
        answer[0][0] = maps[0][0]
    else:
        for j in range(i + 1):
            if j == 0:
                answer[i][j] = answer[i - 1][j] + maps[i][j]
            elif j == i:
                answer[i][j] = answer[i - 1][j - 1] + maps[i][j]
            else:
                answer[i][j] = max(answer[i - 1][j - 1], answer[i - 1][j]) + maps[i][j]

print(max(answer[N - 1]))
