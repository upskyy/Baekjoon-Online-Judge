n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

 
def dfs(idx, s):
    global answer
    if idx >= n:
        if answer < s:
            answer = s
        return

    if idx + arr[idx][0] <= n:
        dfs(idx + arr[idx][0], s + arr[idx][1])
    dfs(idx + 1, s)


dfs(0, 0)
print(answer)
