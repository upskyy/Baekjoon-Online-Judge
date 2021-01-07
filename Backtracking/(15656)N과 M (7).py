import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
idx = 0
answers = [0 for _ in range(M)]


def calculate(index, n, m, nums, answers):
    if index == m:
        for answer in answers:
            print(answer, end=' ')
        print()
        return

    for i in range(1, n + 1):
        answers[index] = nums[i - 1]
        calculate(index + 1, n, m, nums, answers)


calculate(idx, N, M, nums, answers)
