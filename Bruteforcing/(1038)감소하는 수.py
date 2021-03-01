N = int(input())


def forward(N):
    cnt = 0
    num = 1
    while True:
        str_num = str(num)
        flag = True
        if num < 10:
            pass
        else:
            for i in range(1, len(str_num)):
                if str_num[i - 1] > str_num[i]:
                    continue
                else:
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    flag = False
                    break

        if flag:
            cnt += 1
            if cnt == N:
                return num
            num += 1


if N >= 1023:
    print(-1)
elif N == 0:
    print(0)
else:
    print(forward(N))
