import sys

input = sys.stdin.readline
N, M = map(int, input().split())

num = 0
answers = [0 for _ in range(M)]


def calculate(index, num, n, m, answers):
    if index == m:
        for answer in answers:
            print(answer, end=' ')
        print()
        return

    for i in range(num + 1, n + 1):
        answers[index] = i
        calculate(index + 1, i, n, m, answers)


calculate(num, num, N, M, answers)

