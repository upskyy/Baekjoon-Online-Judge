N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    flag = False
    start = 0
    last = len(cards) - 1

    while start <= last:
        mid = (start + last) // 2
        if num == cards[mid]:
            print(1, end=' ')
            flag = True
            break
        elif cards[mid] > num:
            last = mid - 1
        elif cards[mid] < num:
            start = mid + 1

    if not flag:
        print(0, end=' ')

print()