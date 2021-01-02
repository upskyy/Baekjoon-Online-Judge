import sys

input = sys.stdin.readline
num = int(input())

answer = [0 for _ in range(num + 1)]
for i in range(1, num + 1):
    answer[i] = i
    j = 1
    while j * j <= i:
        if answer[i] > answer[i - j * j] + 1:
            answer[i] = answer[i - j * j] + 1
        j += 1

print(answer[num])
