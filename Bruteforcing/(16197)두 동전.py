N, M = map(int, input().split())
maps = list()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
x1, y1 = (0, 0)
x2, y2 = (0, 0)
flag = False
for i in range(N):
    temp = list()
    for j, x in enumerate(input()):
        if x == 'o':
            x = '.'
            if not flag:
                x1 = i
                y1 = j
                flag = True
            else:
                x2 = i
                y2 = j
        temp.append(x)
    maps.append(temp)


def forward(idx, x1, y1, x2, y2):
    answer = -1
    if idx == 11:
        return -1
    flag1 = False
    flag2 = False
    if x1 < 0 or x1 >= N or y1 < 0 or y1 >= M:
        flag1 = True
    if x2 < 0 or x2 >= N or y2 < 0 or y2 >= M:
        flag2 = True

    if flag1 and flag2:
        return -1

    if flag1 or flag2:
        return idx

    for i in range(4):
        new_x1 = x1 + dx[i]
        new_y1 = y1 + dy[i]
        new_x2 = x2 + dx[i]
        new_y2 = y2 + dy[i]
        if 0 <= new_x1 < N and 0 <= new_y1 < M and maps[new_x1][new_y1] == '#':
            new_x1 = x1
            new_y1 = y1
        if 0 <= new_x2 < N and 0 <= new_y2 < M and maps[new_x2][new_y2] == '#':
            new_x2 = x2
            new_y2 = y2

        cnt = forward(idx + 1, new_x1, new_y1, new_x2, new_y2)
        if cnt == -1:
            continue
        else:
            if answer == -1 or answer > cnt:
                answer = cnt

    return answer

print(forward(0, x1, y1, x2, y2))
