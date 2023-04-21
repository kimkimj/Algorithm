n, m = map(int, input().split())
arr = list(map(int, input().split()))

sums = [0] * n
sums[0] = arr[0]
for i in range(1, n):
    sums[i] += arr[i] + sums[i - 1]

answer = [0] * m

for a in range(m):
    i, j = map(int, input().split())
    if i > 1:
        answer[a] = sums[j - 1] - sums[i - 2]
    else:
        answer[a] = sums[j - 1]

for i in range(m):
    print(answer[i])