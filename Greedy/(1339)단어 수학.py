N = int(input())
strings = list()
alphabets = [0 for i in range(26)]

for _ in range(N):
    strings.append(input())


for string in strings:
    i = 0
    while string:
        alphabet = string[-1]
        alphabets[ord(alphabet) - ord('A')] += (10 ** i)
        i += 1
        string = string[:-1]

alphabets.sort(reverse=True)
answer = 0

for i in range(9, -1, -1):
    answer += i * alphabets[9 - i]

print(answer)
