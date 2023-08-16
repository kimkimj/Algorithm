def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    for i in range(4):
        dp[0][i] = land[0][i]

    for row in range(1, len(land)):
        for col in range(4):
            sums = []
            for i in range(4):
                if i != col:
                    sums.append(dp[row - 1][i])
            dp[row][col] = max(sums) + land[row][col]

    return max(dp[len(land) - 1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
