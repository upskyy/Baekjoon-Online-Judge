N = int(input())
times = list(map(int, input().split()))

times.sort()

sum_value = 0
answer = 0

for time in times:
    sum_value += time
    answer += sum_value

print(answer)
