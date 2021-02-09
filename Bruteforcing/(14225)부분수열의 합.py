from itertools import combinations

N = int(input())
nums_list = list(map(int, input().split()))
check = [False for _ in range(sum(nums_list) + 1)]
finish = False

for i in nums_list:
    check[i] = True

for j in range(2, len(nums_list) + 1):
    for combination in combinations(nums_list, j):
        check[sum(combination)] = True

check[0] = True

for idx, flag in enumerate(check):
    if flag:
        continue
    else:
        print(idx)
        finish = True
        break

if not finish:
    print(len(check))
