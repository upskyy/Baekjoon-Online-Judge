# 재귀함수를 이용한 백트래킹

import sys

input = sys.stdin.readline
num_seats = int(input())
num_fixed_seats = int(input())
fixed_seats = [False for _ in range(num_seats)]
for _ in range(num_fixed_seats):
    fixed_seats[int(input()) - 1] = True
answer = list()


def calculate(num_seats, num_select, fixed_seats, answer, change_flag):
    if num_select == (num_seats - 1):
        answer.append(0)
        return
    if fixed_seats[num_select] or fixed_seats[num_select + 1] or change_flag:
        calculate(num_seats, num_select + 1, fixed_seats, answer, change_flag=False)
        return

    calculate(num_seats, num_select + 1, fixed_seats, answer, change_flag=True)
    calculate(num_seats, num_select + 1, fixed_seats, answer, change_flag=False)


calculate(num_seats, 0, fixed_seats, answer, False)
print(len(answer))



# 피보나치 수열 이용

import sys

input = sys.stdin.readline
num_seats = int(input())
numbers = [1 for _ in range(num_seats + 1)]
num_fixed_seats = int(input())
temp = 0
vip = 0
answer = 1

for i in range(2, num_seats + 1):
    numbers[i] = numbers[i - 1] + numbers[i - 2]

for _ in range(num_fixed_seats):
    vip = int(input())
    answer *= numbers[vip - temp - 1]
    temp = vip

answer *= numbers[num_seats - vip]
print(answer)
