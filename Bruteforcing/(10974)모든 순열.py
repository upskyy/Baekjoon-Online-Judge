from itertools import permutations
import sys

input = sys.stdin.readline
n = int(input())
permutation = [value for value in range(1, n + 1)]
answers = permutations(permutation)
for answer in answers:
    print(" ".join(map(str, answer)))
