n = int(input())

arr = list(map(int, input().split()))
dp = []
dp.append(1)

for i in range(1, len(arr)):
    lcs = 1
    for j in range(i):
        if arr[j] < arr[i]:
            lcs = max(lcs, dp[j] + 1)
    dp.append(lcs)

print(max(dp))