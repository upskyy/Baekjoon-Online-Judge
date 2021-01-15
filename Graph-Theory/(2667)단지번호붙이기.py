from collections import Counter
from functools import reduce

num = int(input())
a = [list(map(int, list(input()))) for _ in range(num)]
group = [[0] * num for _ in range(num)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0


def dfs(x, y, cnt):
    group[x][y] = cnt
    for k in range(4):
        new_x, new_y = x + dx[k], y + dy[k]
        if 0 <= new_x < num and 0 <= new_y < num:
            if a[new_x][new_y] == 1 and group[new_x][new_y] == 0:
                dfs(new_x, new_y, cnt)


for i in range(num):
    for j in range(num):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            dfs(i, j, cnt)

answers = reduce(lambda x, y: x + y, group)
answers = [x for x in answers if x > 0]
answers = sorted(list(Counter(answers).values()))
print(cnt)
print('\n'.join(map(str, answers)))
