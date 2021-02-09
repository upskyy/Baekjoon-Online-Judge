k = int(input())
operator = input().split()
check = [False for _ in range(10)]
max_value = ''
min_value = ''


def calculate(i, j, k):
    if k == '<':
        return i < j
    elif k == '>':
        return i > j


def dfs(idx, temp):
    global max_value, min_value

    if idx == (k + 1):  # 마지막까지 온 경우
        if not len(min_value):  # min_value에 값이 없다면 처음이니까 최소값
            min_value = temp
        else:
            max_value = temp
        return

    for i in range(10):
        if not check[i]:
            if idx == 0 or calculate(temp[-1], str(i), operator[idx - 1]):
                check[i] = True
                dfs(idx + 1, temp + str(i))
                check[i] = False


dfs(0, "")
print(max_value)
print(min_value)
