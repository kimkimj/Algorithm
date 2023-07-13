import sys
input = sys.stdin.readline

n, target = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
answer = 0

while start <= end:
    mid = (start + end) // 2

    total = 0
    for h in trees:
        if h > mid:
            total += h - mid

    if total >= target:
        answer = mid
        start = mid + 1

    else:
        end = mid - 1

print(answer)