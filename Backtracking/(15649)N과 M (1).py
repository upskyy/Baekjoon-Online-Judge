import sys

input = sys.stdin.readline
N, M = map(int, input().split())

idx = 0
check = [False for _ in range(N + 1)]
answers = [0 for _ in range(M)]


def calculate(index, n, m, check, answers):
    if index == m:
        for answer in answers:
            print(answer, end=' ')
        print()
        return

    for i in range(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        answers[index] = i
        calculate(index + 1, n, m, check, answers)
        check[i] = False


calculate(idx, N, M, check, answers)

