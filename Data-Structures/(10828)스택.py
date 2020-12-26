import sys

input = sys.stdin.readline

stack = list()
num = int(input())
for _ in range(num):
    cmd = input().rstrip().split()

    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if not stack:
            print("-1")
        else:
            top = stack.pop()
            print(top)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if not stack:
            print("1")
        else:
            print("0")
    elif cmd[0] == 'top':
        if not stack:
            print("-1")
        else:
            print(stack[-1])
