N = int(input())

nums = list()
for _ in range(N):
    nums.append(int(input()))

nums.sort()
answer = nums[0]
best_cnt = 1
cnt = 1

for n in range(len(nums)):
    if n == 0:
        continue
    if nums[n] == nums[n - 1]:
        cnt += 1
    else:
        cnt = 1
    if best_cnt < cnt:
        best_cnt = cnt
        answer = nums[n]

print(answer)
