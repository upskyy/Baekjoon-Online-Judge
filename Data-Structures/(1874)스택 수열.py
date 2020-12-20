import sys

input = sys.stdin.readline

num = int(input())
stack = list()
ops =list()
m = 0
for _ in range(num):
    value = int(input())
    if(value > m):
        while(value > m):
            m = m + 1
            stack.append(m)
            ops.append('+')
        stack.pop()
        ops.append('-')
    else:
        found = False
        if stack:
            top = stack.pop()
            ops.append('-')
            if(top == value):
                found = True
        if (found == False):
            print('NO')
            sys.exit()
for op in ops:
    print(op)