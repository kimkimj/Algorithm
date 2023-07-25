T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    i = 0
    while i < n * m:
        dp.append(arr[i : i + m])
        i += m

    for j in range(1, m):
        for i in range(n):

            # 왼쪽 위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 왼쪽
            left = dp[i][j - 1]

            # 왼쪽 아래
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            dp[i][j] += max([left, left_down, left_up])

    # 마지막 column 돌면서 가장 큰 수 찾기
    answer = 0
    for i in range(n):
        answer = max(answer, dp[i][m - 1])

    print(answer)



2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2