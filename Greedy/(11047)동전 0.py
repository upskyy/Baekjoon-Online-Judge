N, K = map(int, input().split())
coins = list()
count = 0
for _ in range(N):
    coins.append(int(input()))

coins = coins[:: -1]

for coin in coins:
    if K // coin == 0:
        continue
    else:
        count += (K // coin)
        K %= coin

print(count)
