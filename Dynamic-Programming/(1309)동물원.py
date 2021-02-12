N = int(input())

maps = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    if i == 0:
        maps[i][0] = 1
        maps[i][1] = 1
        maps[i][2] = 1
    else:
        maps[i][0] = (maps[i - 1][0] + maps[i - 1][1] + maps[i - 1][2]) % 9901
        maps[i][1] = (maps[i - 1][0] + maps[i - 1][2]) % 9901
        maps[i][2] = (maps[i - 1][0] + maps[i - 1][1]) % 9901

answer = sum(maps[N - 1]) % 9901
print(answer)
