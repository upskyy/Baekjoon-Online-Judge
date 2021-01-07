import sys

input = sys.stdin.readline
num = int(input())

start = 1
end = 9
length = 1
answer = 0
flag = False
while True:
    if end > num:
        end = num
        flag = True
    answer += (end - start + 1) * length
    if flag:
        print(answer)
        break
    length += 1
    start *= 10
    end = (start * 10) - 1


