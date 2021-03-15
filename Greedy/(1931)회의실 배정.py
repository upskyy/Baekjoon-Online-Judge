N = int(input())
meetings = list()
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings = sorted(meetings, key=lambda a: a[0])
meetings = sorted(meetings, key=lambda a: a[1])

last = 0
answer = 0
for meeting in meetings:
    if last <= meeting[0]:
        answer += 1
        last = meeting[1]

print(answer)
