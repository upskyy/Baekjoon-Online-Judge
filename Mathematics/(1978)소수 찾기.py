import sys

input = sys.stdin.readline

_ = int(input())
numbers = input().split()
count = 0

for number in numbers:
    flag = False
    if int(number) == 1:
        continue
    for i in range(2, int(int(number) ** 0.5) + 1, 1):
        if not int(number) % i:
            flag = True
            break
    if not flag:
        count += 1

print(count)
