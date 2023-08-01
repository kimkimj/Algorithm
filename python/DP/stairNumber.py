# https://velog.io/@minchoul2/%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98-Python
# 다른 풀이
# https://ji-gwang.tistory.com/275
n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(1, n):
    dp[n][0] = dp[n - 1][1]
    dp[n][9] = dp[n - 1][8]

    for k in range(1, 9):
        dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k + 1]

print(sum(dp[n - 1] % 1000000000))