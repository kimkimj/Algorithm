import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 맨 앞에 0을 넣어 인덱스를 맞춰준다
sums = [0]
total = 0
for i in range(n):
    total += arr[i]
    sums.append(total)

for _ in range(m):
    i, j = map(int, input().split())
    print(sums[j] - sums[i - 1])