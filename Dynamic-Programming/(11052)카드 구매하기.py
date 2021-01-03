import sys

input = sys.stdin.readline
num = int(input())
card_price = list(map(int, input().split()))
card_price.insert(0, 0)
answer = [0 for _ in range(num + 1)]
for i in range(1, num + 1):
    answer[i] = i * card_price[1]
    j = 1
    while j <= i:
        if answer[i] < answer[i - j] + card_price[j]:
            answer[i] = answer[i - j] + card_price[j]
        j += 1
print(answer[num])
