N = int(input())
cards = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))
dictionary = dict()

for num in nums:
    dictionary[num] = 0

for card in cards:
    if card not in dictionary.keys():
        continue
    else:
        dictionary[card] += 1

for num in nums:
    print(dictionary[num], end=' ')

print()