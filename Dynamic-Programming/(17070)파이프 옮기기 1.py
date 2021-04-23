n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

check = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
check[0][1][0] = 1

for i in range(n):
    for j in range(2, n):
        if not maps[i][j]:
            if not maps[i][j - 1]:
                check[i][j][0] += check[i][j - 1][0]
                check[i][j][0] += check[i][j - 1][2]
            if 0 <= i - 1 < n and not maps[i - 1][j] and not maps[i][j - 1] and not maps[i - 1][j - 1]:
                check[i][j][2] += check[i - 1][j - 1][0]
                check[i][j][2] += check[i - 1][j - 1][1]
                check[i][j][2] += check[i - 1][j - 1][2]
            if 0 <= i - 1 < n and not maps[i - 1][j]:
                check[i][j][1] += check[i - 1][j][1]
                check[i][j][1] += check[i - 1][j][2]

print(sum(check[n - 1][n - 1]))