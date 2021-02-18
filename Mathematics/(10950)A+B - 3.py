N = int(input())
nums = list()
for _ in range(N):
    nums.append(list(map(int, input().split())))

for num in nums:
    print(sum(num))
