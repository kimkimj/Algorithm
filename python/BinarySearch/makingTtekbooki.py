import sys
input = sys.stdin.readline

n, min_height = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2

    total = 0
    for h in arr:
        total += max(0, h - mid)

    if total >= min_height:
        result = mid
        start = mid + 1

    else:
        end = mid - 1
print(result)