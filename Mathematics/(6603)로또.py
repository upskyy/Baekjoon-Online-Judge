from itertools import combinations

while True:
    num_list = list(map(int, input().split()))
    if num_list[0] == 0:
        break

    num_list = num_list[1:]
    combination = list(combinations(num_list, 6))

    for numbers in combination:
        numbers = list(map(str, numbers))
        print(" ".join(numbers))

    print()
