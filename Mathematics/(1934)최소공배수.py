import sys

input = sys.stdin.readline

num = int(input())
for _ in range(num):
    number = input().split()
    a = int(number[0])
    b = int(number[1])
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    print(int((int(number[0]) * int(number[1])) / a))
