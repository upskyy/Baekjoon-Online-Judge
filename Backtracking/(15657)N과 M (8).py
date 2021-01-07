import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
num = 0
answers = [0 for _ in range(M)]


def calculate(index, num, n, m, nums, answers):
    if index == m:
        for answer in answers:
            print(answer, end=' ')
        print()
        return

    for i in range(num, n):
        answers[index] = nums[i]
        calculate(index + 1, i, n, m, nums, answers)


calculate(num, num, N, M, nums, answers)
