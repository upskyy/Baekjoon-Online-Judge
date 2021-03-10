import sys

N, K = map(int, input().split())


def calculate(num):
    lengths = 0
    for i in range(len(str(num))):
        if i == 0:
            start = 1
        else:
            start = 10 ** i
        end = 10 * start - 1
        if end > num:
            end = num

        lengths += ((end - start) + 1) * (i + 1)

    return lengths


left = 1
right = N
answer = 0

if calculate(N) < K:
    print(-1)
    sys.exit(0)

while left <= right:
    mid = (left + right) // 2
    if calculate(mid) < K:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1


str_answer = str(answer)
l = calculate(answer)
print(str_answer[len(str_answer) - (l - K) - 1])
