import sys

input = sys.stdin.readline

num = input().split()
answers = list()
check = [False] * (int(num[1]) + 1)
for i in range(2, int(num[1]) + 1, 1):
    if not check[i]:
        answers.append(i)
        for j in range(i + i, int(num[1]) + 1, i):
            check[j] = True

for answer in answers:
    if answer >= int(num[0]):
        print(answer)
