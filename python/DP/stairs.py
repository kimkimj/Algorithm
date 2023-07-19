n = int(input())
arr = [int(input()) for _ in range(n)]

d = [0] * len(arr)
d[0] = arr[0]
d[1] = arr[0] + arr[1]
d[2] = max(arr[0] + arr[2], arr[1] + arr[2])

for i in range(3, len(arr)):
    d[i] = max(d[i - 3] + arr[i - 1] + arr[i], d[i - 2] + arr[i])
print(d[n - 1])