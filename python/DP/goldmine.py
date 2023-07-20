T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0] * (n * m)

    for i in range(n * m):
        if i % m == 0:
            dp[i] = arr[i]
        if i % m != m - 1: # 오른쪽이 없어서 -m해야 하는데 그럼 잘못된 값이 나옴
            dp[i + 1] = max(dp[i + 1], dp[i] + arr[i + 1])

            if i - n >= 0:
                dp[i - n] = max(dp[i - n], dp[i] + arr[i - n])

            if i + m + 1 < m * n:
                dp[i + m + 1] = max(dp[i + m + 1], dp[i] + arr[i + m + 1])
    print(dp[n * m - 1])





