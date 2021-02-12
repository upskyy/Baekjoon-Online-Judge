T = int(input())

for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    maps = [[0, 0, 0] for _ in range(N)]

    for i in range(N):
        if i == 0:
            maps[i][1] = score[0][i]
            maps[i][2] = score[1][i]

        else:
            maps[i][0] = max(maps[i - 1][0], maps[i - 1][1], maps[i - 1][2])
            maps[i][1] = max(maps[i - 1][0], maps[i - 1][2]) + score[0][i]
            maps[i][2] = max(maps[i - 1][0], maps[i - 1][1]) + score[1][i]

    print(max(maps[N - 1]))
