import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
req = list(map(int, input().split()))


for target in req:
    found = False
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            found = True
            break

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    if found:
        print("yes")
    else:
        print("no")

