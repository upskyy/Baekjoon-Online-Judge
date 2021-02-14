import sys

year = int(input())

if year % 4 == 0:
    if year % 100 != 0:
        print(1)
        sys.exit()

if year % 400 == 0:
    print(1)
    sys.exit()

print(0)
