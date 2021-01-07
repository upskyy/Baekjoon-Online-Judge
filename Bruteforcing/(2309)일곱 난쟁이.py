import sys

input = sys.stdin.readline
inputs = list()
for _ in range(9):
    inputs.append(int(input()))

for i in range(8):
    for j in range(i + 1, 9):
        if (sum(inputs) - inputs[i] - inputs[j]) == 100:
            inputs[i] = inputs[j] = 0
            inputs.sort()
            for num in inputs:
                if not num:
                    continue
                else:
                    print(num)
            sys.exit(0)

