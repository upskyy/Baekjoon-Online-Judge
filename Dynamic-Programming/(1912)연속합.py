import sys

input = sys.stdin.readline
_ = int(input())
numbers = list(map(int, input().split()))
answer = list()
for i, number in enumerate(numbers):
    if i == 0:
        answer.append(number)
    else:
        if number > answer[i - 1] + number:
            answer.append(number)
        else:
            answer.append(answer[i - 1] + number)

print(max(answer))
