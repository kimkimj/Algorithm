n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])
length = max(dp)
print(length)

subsequence = []
order = length
for i in range(n - 1, -1, -1):
    if dp[i] == order:
        subsequence.append(arr[i])
        order -= 1

subsequence.reverse()
print(*subsequence)

# 8
# 10 20 10 10 40 20 30 40