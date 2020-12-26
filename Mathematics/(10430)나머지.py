import sys

input = sys.stdin.readline

num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
