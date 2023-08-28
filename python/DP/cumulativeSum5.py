import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

for r in range(1, n + 1):
    for c in range(1, n + 1):
        # arr은 첫 줄과 행에 0 버프가 없으므로 1을 빼줘야한다
        dp[r][c] = dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1] + arr[r - 1][c - 1]

for _ in range(m):
    r1, c1, r2, c2 =  map(int,input().split())
    result = dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1 - 1]
    print(result)