from itertools import combinations

N = int(input())
potential = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
min_gap = float('inf')
team_list = list()

for team in list(combinations(members, N // 2)):
    team_list.append(team)

for i in range(len(team_list) // 2):
    first_team = team_list[i]
    first_sum = 0
    for A_member in first_team:
        for k in first_team:
            first_sum += potential[A_member][k]

    second_team = team_list[- 1 - i]
    second_sum = 0
    for B_member in second_team:
        for k in second_team:
            second_sum += potential[B_member][k]

    min_gap = min(min_gap, abs(first_sum - second_sum))

print(min_gap)

