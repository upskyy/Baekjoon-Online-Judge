import sys
input = sys.stdin.readline

num = int(input())
count = 0
count += int(num / 5)
count += int(num / 25)
count += int(num / 125)
print(count)
