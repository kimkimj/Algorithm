import sys
input = sys.stdin.readline

n, req = map(int, input().split())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

start = 0
end = max(arr)
result = 1

while start <= end:
    total = 0
    mid = (start + end) // 2

    if mid < 2:
        mid = 1

    for line in arr:
        total += line // mid

    if total >= req:
        start = mid + 1
        result = mid

    else:
        end = mid -1

print(result)