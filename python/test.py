import sys
input = sys.stdin.readline().rstrip
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
req = list(map(int, input().split()))

for num in arr:
    result = binary_search(arr, num, 0, len(arr) - 1)
    if result == None:
        print("No", end =' ')
    else:
        print("Yes", end = ' ')