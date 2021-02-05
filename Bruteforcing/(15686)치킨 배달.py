from itertools import combinations

N, M = map(int, input().split())
maps = list()

for _ in range(N):
    maps.append(list(map(int, input().split())))
chicken = list()
house = list()

for i, map in enumerate(maps):
    for j, n in enumerate(map):
        if n == 1:
            house.append((i, j))
        elif n == 2:
            chicken.append((i, j))


min_value = float('inf')
for comb in combinations(chicken, M):
    sum_value = 0
    for i1, j1 in house:
        sum_value += min([abs(i1 - c[0]) + abs(j1 - c[1]) for c in comb])
        if min_value <= sum_value:
            break
    if sum_value < min_value:
        min_value = sum_value

print(min_value)

