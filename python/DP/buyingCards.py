n = int(input())
cards = list(map(int, input().split()))

dp = [0] * n
dp[0] = cards[0]
if len(cards) > 1:
    dp[1] = max(cards[0] * 2, cards[1])

for i in range(2, n):
    a =dp[i - 1] + dp[1]
    b= dp[i -2] + dp[0]
    dp[i] = max(dp[i - 1] + dp[1], dp[i -2] + dp[0])
    if i <= len(cards):
        dp[i] = max(cards[i], dp[i])

print(dp[n - 1])