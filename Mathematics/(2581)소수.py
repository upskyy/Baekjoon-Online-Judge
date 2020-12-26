import sys

input = sys.stdin.readline

num1 = int(input())
num2 = int(input())

answers = list()
check = [False] * (num2 + 1)
for i in range(2, num2 + 1, 1):
    if not check[i]:
        answers.append(i)
        for j in range(i + i, num2 + 1, i):
            check[j] = True

ans = [answer for answer in answers if answer >= num1]
if not len(ans):
    print(-1)
else:
    print(sum(ans))
    print(min(ans))
