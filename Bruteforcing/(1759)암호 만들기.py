import sys

input = sys.stdin.readline
L, _ = map(int, input().split())
characters = input().split()
characters.sort()
answer = str()


def check(answer):
    VOWEL = ['a', 'e', 'i', 'o', 'u']
    vowel = 0  # 모음
    consonant = 0  # 자음

    for char in answer:
        if char in VOWEL:
            vowel += 1
        else:
            consonant += 1

    if vowel >= 1 and consonant >= 2:
        return True
    else:
        return False


def calculate(L, characters, answer, idx):
    if len(answer) == L:
        if check(answer):
            print("".join(answer))
            return
        else:
            return

    if idx >= len(characters):
        return

    calculate(L, characters, answer + characters[idx], idx + 1)
    calculate(L, characters, answer, idx + 1)


calculate(L, characters, answer, 0)


