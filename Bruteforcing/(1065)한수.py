num = int(input())
cnt = 99
if num < 100:
    cnt = num
else:
    for n in range(101, num + 1):
        n = list(map(int, str(n)))
        if n[0] - n[1] == n[1] - n[2]:
            cnt += 1

print(cnt)
