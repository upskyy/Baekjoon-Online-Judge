H, M = map(int, input().split())

if M - 45 < 0:
    if H - 1 < 0:
        H = 23
        M += 15
    else:
        H -= 1
        M += 15
else:
    M -= 45

print(H, end=' ')
print(M)
