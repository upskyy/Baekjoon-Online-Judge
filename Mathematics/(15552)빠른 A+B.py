import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    print(sum(list(map(int, input().split()))))

