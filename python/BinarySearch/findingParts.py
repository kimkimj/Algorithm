import sys
input = sys.stdin.readline

n = int(input())
parts = list(map(int, input().split()))
parts.sort()

m = int(input())
req = list(map(int, input().split()))

for i in range(m):
    found = False
    target = req[i]
    start = 0
    end = n - 1
    while start <= end and not found:
        mid = (start + end) // 2

        if parts[mid] < target:
            start = mid + 1

        elif parts[mid] > target:
            end = mid - 1

        else:
            found = True

    if found:
        print("yes")
    else:
        print("no")


