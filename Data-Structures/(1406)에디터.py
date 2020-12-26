import sys

input = sys.stdin.readline

left_stack = list(input()[:-1])  # 개행문자(\n) 빼기 위해서
right_stack = list()

num = int(input())
for _ in range(num):
    cmd = input()
    if (cmd[0] == 'L') and left_stack:
        right_stack.append(left_stack.pop())
    elif (cmd[0] == 'D') and right_stack:
        left_stack.append(right_stack.pop())
    elif (cmd[0] == 'B') and left_stack:
        left_stack.pop()
    elif cmd[0] == 'P':
        left_stack.append(cmd[2])

print("".join(left_stack + right_stack[::-1]))
