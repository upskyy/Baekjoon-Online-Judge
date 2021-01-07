import sys

input = sys.stdin.readline
N, M = map(int, input().split())
answers = [0 for _ in range(M)]


def calculate(index, num, n, m, answers):
    if index == m:
        for answer in answers:
            print(answer, end=' ')
        print()
        return

    for i in range(num, n + 1):
        answers[index] = i
        calculate(index + 1, i, n, m, answers)


calculate(0, 1, N, M, answers)
