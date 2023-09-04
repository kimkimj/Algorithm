digit = int(input())
dp = [[0] * 10 for _ in range(digit + 1)]

for i in range(1, 10):
    dp[1][i] = i

for i in range(1, digit):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][9]

    for k in range(1, 9):
        dp[i][k] = dp[i - 1][k - 1] + dp[i - 1][k + 1]

print(sum(dp[digit - 1]) % 1000000000)