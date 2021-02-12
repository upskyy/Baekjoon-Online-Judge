N = int(input())
sequence = list(map(int, input().split()))

answer = [0 for _ in range(N)]
for i in range(N):
    answer[i] = sequence[i]
    for j in range(i):
        if (sequence[j] < sequence[i]) and (answer[i] < answer[j] + sequence[i]):
            answer[i] = answer[j] + sequence[i]

print(max(answer))
