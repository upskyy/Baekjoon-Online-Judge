import sys
input = sys.stdin.readline

stack = list()
count = 0
flag = False
brackets = input()[:-1]
for bracket in brackets:
    if bracket == '(':
        stack.append(bracket)
        flag = True
    else:
        if flag:
            stack.pop()
            count += len(stack)
            flag = False
        else:
            stack.pop()
            count += 1
print(count)