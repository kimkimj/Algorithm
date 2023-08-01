T = int(input())
for _ in range(T):
    n = int(input())

    dp = [1] * (n + 1)
    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2]

    print(dp[n])

# 등차 수열: (n - 3) + (n - 3)