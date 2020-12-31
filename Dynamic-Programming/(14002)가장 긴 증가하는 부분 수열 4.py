import sys

input = sys.stdin.readline
num = int(input())
sequence = list(map(int, input().split()))
record = [-1 for _ in range(num)]
ans = [1 for _ in range(num)]
for i in range(num):
    for j in range(i):
        if (sequence[j] < sequence[i]) and (ans[i] < ans[j] + 1):
            ans[i] = ans[j] + 1
            record[i] = j
max_length = max(ans)
print(max_length)
idx = ans.index(max_length)


def output(p):
    if p == -1:
        return
    output(record[p])
    print(sequence[p], end=' ')


output(idx)
print()
