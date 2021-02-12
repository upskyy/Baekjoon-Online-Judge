N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]

answer = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    if i == 0:
        answer[i][0] = costs[0][0]
        answer[i][1] = costs[0][1]
        answer[i][2] = costs[0][2]
    else:
        answer[i][0] = min(answer[i - 1][1], answer[i - 1][2]) + costs[i][0]
        answer[i][1] = min(answer[i - 1][0], answer[i - 1][2]) + costs[i][1]
        answer[i][2] = min(answer[i - 1][0], answer[i - 1][1]) + costs[i][2]

print(min(answer[N - 1]))
