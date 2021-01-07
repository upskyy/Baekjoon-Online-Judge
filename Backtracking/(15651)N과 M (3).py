import sys

input = sys.stdin.readline
N, M = map(int, input().split())

idx = 0
answers = [0 for _ in range(M)]


def calculate(index, n, m, answers):
    if index == m:
        for answer in answers:
            print(answer, end=' ')
        print()
        return

    for i in range(1, n + 1):
        answers[index] = i
        calculate(index + 1, n, m, answers)


calculate(idx, N, M, answers)

