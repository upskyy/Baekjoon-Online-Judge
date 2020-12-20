import sys

input = sys.stdin.readline
num = int(input())
for _ in range(num):
    string = input()
    sentence = list()
    stack1 = list()
    stack2 = list()
    for j in string:
        sentence.append(j)
    sentence.append('\n')
    for ch in sentence:
        if((ch == ' ') or (ch == '\n')):
            while(len(stack1)!=0):
                top = stack1.pop()
                stack2.append(top)
            if(ch != '\n'):
                stack2.append(' ')
        else:
            stack1.append(ch)
    print("".join(stack2))