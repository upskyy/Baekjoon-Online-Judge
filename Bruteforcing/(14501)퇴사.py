import sys

input = sys.stdin.readline
num = int(input())
time = [0 for _ in range(15)]
pay = [0 for _ in range(15)]
for i in range(num):
    time[i], pay[i] = map(int, input().split())
answer = list()


def calculate(num, day, sum, time, pay):
    if day > (num + 1):
        return
    if day == (num + 1):
        answer.append(sum)
        return

    calculate(num, day + time[day - 1], sum + pay[day - 1], time, pay)
    calculate(num, day + 1, sum, time, pay)


calculate(num, 1, 0, time, pay)
print(max(answer))
