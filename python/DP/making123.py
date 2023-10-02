n = 4

dp = [0, 1, 2, 4]

for i in range(4, n + 1):
    total = dp[i - 1] + dp[i - 2] + dp[i - 3]
    dp.append(total)

print(dp[n])