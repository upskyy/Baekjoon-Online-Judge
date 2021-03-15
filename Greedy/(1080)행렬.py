N, M = map(int, input().split())

matrix_A = [list(map(int, list(input()))) for _ in range(N)]
matrix_B = [list(map(int, list(input()))) for _ in range(N)]
answer = 0


def flip(x, y):
    for p in range(x - 1, x + 2, 1):
        for q in range(y - 1, y + 2, 1):
            matrix_A[p][q] = 1 - matrix_A[p][q]


for i in range(N - 2):
    for j in range(M - 2):
        if matrix_A[i][j] != matrix_B[i][j]:
            answer += 1
            flip(i + 1, j + 1)

for i in range(N):
    for j in range(M):
        if matrix_A[i][j] != matrix_B[i][j]:
            print(-1)
            exit()

print(answer)
