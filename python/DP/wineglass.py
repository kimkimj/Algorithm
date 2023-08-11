# 이전까지 구한 dp값보다 현재 와인을 마심으로써 구한 dp값이 작다면 현재 와인을 마시지 말아야 한다.

n = int(input())
arr = [0] * n
for i in range(n):
    arr[i] = int(input())

dp = [0] * n
dp[0] = arr[0]

if n > 1:
    dp[1] = arr[0] + arr[1]

for i in range(2, n):
    dp[i] = arr[i] + dp[i - 3] + max(arr[i - 2], arr[i - 1])
    dp[i] = max(dp[i], dp[i - 1])

print(dp[n - 1])