num_test = int(input())
for _ in range(num_test):
    n = int(input())

    dp = [[1, 0], [0, 1]]

    for i in range(2, n + 1):
        zero_1, one_1 = dp[i - 1]
        zero_2, one_2 = dp[i - 2]

        dp.append([zero_1 + zero_2, one_1 + one_2])

    print(*dp[n])