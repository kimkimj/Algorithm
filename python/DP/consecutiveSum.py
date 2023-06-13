n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]

maximum = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])
    maximum = max(dp[i], maximum)
print(maximum)

    # 10, -4, 3, 1, 5, 6, -35, 12, 21, -1
    # 10  6  9  10  15 21  -14 12 33 32