from collections import deque

num_computer = int(input())
N = int(input())
maps = dict()
check = [False for _ in range(num_computer + 1)]
answer = 0
for _ in range(N):
    n1, n2 = map(int, input().split())
    if n1 in maps.keys():
        maps[n1].append(n2)
    else:
        maps[n1] = list()
        maps[n1].append(n2)
    if n2 in maps.keys():
        maps[n2].append(n1)
    else:
        maps[n2] = list()
        maps[n2].append(n1)


def bfs(start):
    global answer
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        if x in maps.keys():
            for num in maps[x]:
                if not check[num]:
                    q.append(num)
                    answer += 1
                    check[num] = True


bfs(1)
print(answer - 1)
