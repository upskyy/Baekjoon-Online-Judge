import sys

input = sys.stdin.readline

num = int(input())
for _ in range(num):
    sentence = input()
    cnt = 0
    flag = 0
    for j in sentence:
        if j == '(':
            cnt = cnt + 1
        elif j == ')':
            if cnt == 0:
                print("NO")
                flag = 1
                break
            cnt = cnt - 1
    if flag == 0:
        if cnt == 0:
            print("YES")
        else:
            print("NO")
