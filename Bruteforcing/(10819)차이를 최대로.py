import sys

input = sys.stdin.readline
_ = int(input())
nums = list(map(int, input().split()))
nums.sort()


def max_value(inputs):
    sum_value = 0
    for i in range(1, len(inputs)):
        sum_value += abs(inputs[i - 1] - inputs[i])
    return sum_value


def next_permutation(numbers):
    i = len(numbers) - 1
    while i > 0 and numbers[i] <= numbers[i - 1]:
        i -= 1
    if i == 0:
        return False
    j = len(numbers) - 1
    while numbers[i - 1] >= numbers[j]:
        j -= 1

    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]
    j = len(numbers) - 1
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1
    return True


answer = 0
while True:
    temp = max_value(nums)
    answer = max(temp, answer)
    if not next_permutation(nums):
        break
print(answer)
