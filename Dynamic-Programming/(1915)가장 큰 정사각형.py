N, M = map(int, input().split())
maps = [[int(i) for i in input()] for _ in range(N)]

answer = 0

for i in range(N):
    for j in range(M):
        if i > 0 and j > 0 and maps[i][j] == 1:
            maps[i][j] = min(maps[i - 1][j], maps[i][j - 1], maps[i - 1][j - 1]) + 1

        answer = max(answer, maps[i][j])

print(answer * answer)

