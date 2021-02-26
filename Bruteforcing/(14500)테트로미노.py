N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]


def blue():
    max_value = 0

    for i in range(N):
        for j in range(M):
            if j + 3 >= M:
                break
            max_value = max(max_value, (maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i][j + 3]))

    for i in range(N):
        for j in range(M):
            max_value = max(max_value, (maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 3][j]))

        if i + 3 == (N - 1):
            break

    return max_value


def yellow():
    max_value = 0

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1])

        if (i + 1) == (N - 1):
            break

    return max_value


def purple():
    max_value = 0

    for i in range(N):
        for j in range(M):
            if j + 2 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j + 1])

        if (i + 1) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 2 >= M:
                break
            max_value = max(max_value, maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2])

        if (i + 1) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i + 1][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j + 1])

        if (i + 2) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i + 1][j + 1] + maps[i][j] + maps[i + 1][j] + maps[i + 2][j])

        if (i + 2) == (N - 1):
            break

    return max_value


def green():
    max_value = 0

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j + 1])

        if (i + 2) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i + 1][j] + maps[i + 2][j] + maps[i + 1][j + 1] + maps[i][j + 1])

        if (i + 2) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 2 >= M:
                break
            max_value = max(max_value, maps[i + 1][j] + maps[i + 1][j + 1] + maps[i][j + 1] + maps[i][j + 2])

        if (i + 1) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 2 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 1][j + 2])

        if (i + 1) == (N - 1):
            break

    return max_value


def orange():
    max_value = 0

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 2][j + 1])

        if (i + 2) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i + 2][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j + 1])

        if (i + 2) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j + 1])

        if (i + 2) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 1 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i][j + 1])

        if (i + 2) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 2 >= M:
                break
            max_value = max(max_value, maps[i][j + 2] + maps[i + 1][j + 2] + maps[i + 1][j + 1] + maps[i + 1][j])

        if (i + 1) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 2 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2])

        if (i + 1) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 2 >= M:
                break
            max_value = max(max_value, maps[i + 1][j] + maps[i][j] + maps[i][j + 1] + maps[i][j + 2])

        if (i + 1) == (N - 1):
            break

    for i in range(N):
        for j in range(M):
            if j + 2 >= M:
                break
            max_value = max(max_value, maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j + 2])

        if (i + 1) == (N - 1):
            break

    return max_value


print(max(blue(), yellow(), purple(), green(), orange()))
