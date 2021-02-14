N = int(input())
answer = [0 for _ in range(21)]

for i in range(N + 1):
    if i == 0:
        continue
    elif i == 1:
        answer[i] = 1
    else:
        answer[i] = answer[i - 1] + answer[i - 2]

print(answer[N])
