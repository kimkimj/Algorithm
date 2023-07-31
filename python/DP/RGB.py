n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

dp = [[float("inf")] * 3 for _ in range(n)]
dp[0] = cost[0]


for i in range(n - 1):
    for j in range(3):
        if j <= 1:
            dp[i + 1][2] = min(dp[i + 1][2], dp[i][j] + cost[i + 1][2])

        if j >= 1:
            dp[i + 1][0] = min(dp[i + 1][0], dp[i][j] + cost[i + 1][0])

        if j == 0 or j == 2:
            dp[i + 1][1] = min(dp[i + 1][1], dp[i][j] + cost[i + 1][1])

print(min(dp[n - 1]))

