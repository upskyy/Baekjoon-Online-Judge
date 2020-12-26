import sys

input = sys.stdin.readline

num = input().split()
a = int(num[0])
b = int(num[1])

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print(a)
print(int((int(num[0]) * int(num[1])) / a))
