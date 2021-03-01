money1 = [0, 500, 300, 300, 200, 200, 200, 50, 50, 50, 50]
money2 = [0, 512, 256, 256, 128, 128, 128, 128]

for i in range(5):
    money1.append(30)
for i in range(6):
    money1.append(10)

for i in range(8):
    money2.append(64)
for i in range(16):
    money2.append(32)

T = int(input())

for _ in range(T):
    answer = 0
    a, b = map(int, input().split())

    if a <= 21:
        answer += money1[a]
    if b <= 31:
        answer += money2[b]

    if answer == 0:
        print(0)
    else:
        print(int(str(answer) + '0000'))
