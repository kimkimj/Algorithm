n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0] * n

# edge cases: if n == 1 or n == 2, dp[1],arr[1] or dp[2]arr[2] -> index out of range
if n < 3:
    print(sum(arr))

else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]

     # current stair MUST be incldued (max on the premise that the current stiar is being stepped on)
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, n):
        dp[i] = arr[i] + max(dp[i - 3] + arr[i - 1], dp[i - 2])

    print(dp[n - 1])
