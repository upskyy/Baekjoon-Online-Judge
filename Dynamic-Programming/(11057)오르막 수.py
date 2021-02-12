N = int(input())

num_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N)]

for i in range(N):
    if i == 0:
        for j in range(10):
            num_list[i][j] = 1

    else:
        for j in range(10):
            for k in range(j + 1):
                num_list[i][j] += num_list[i - 1][k]
            num_list[i][j] %= 10007

print(sum(num_list[N - 1]) % 10007)

