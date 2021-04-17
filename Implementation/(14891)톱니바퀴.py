from collections import deque
# N : 0,  S : 1


def check_right(start, dirs):
    if start > 4 or q[start - 1][2] == q[start][6]:
        return

    if q[start - 1][2] != q[start][6]:
        check_right(start + 1, -dirs)
        q[start].rotate(dirs)


def check_left(start, dirs):
    if start < 1 or q[start][2] == q[start + 1][6]:
        return

    if q[start + 1][6] != q[start][2]:
        check_left(start - 1, -dirs)
        q[start].rotate(dirs)


q = dict()
for i in range(1, 5):
    q[i] = deque(list(map(int, input())))

k = int(input())

for _ in range(k):
    num, pos = map(int, input().split())

    check_right(num + 1, -pos)
    check_left(num - 1, -pos)
    q[num].rotate(pos)

answer = 0
for j in range(4):
    if q[j + 1][0] == 1:
        answer += (2 ** j)

print(answer)