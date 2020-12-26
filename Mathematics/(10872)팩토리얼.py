import sys
input = sys.stdin.readline

num = int(input())
ans = 1
for i in range(1, num + 1, 1):
    ans *= i
print(ans)

