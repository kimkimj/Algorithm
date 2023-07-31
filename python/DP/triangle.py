n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(n - 1):
    for j in range(len(arr[i])):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + arr[i + 1][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + arr[i + 1][j + 1])

print(max(dp[n - 1]))
