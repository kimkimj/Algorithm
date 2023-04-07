
n = int(input())
#n_arr = [4, 1, 5, 2, 3]
#n = int(input())
n_arr = list(map(int, input().split()))
#m = 5
m = int(input())
#m_arr = [1, 3, 7, 9, 5]
m_arr = list(map(int, input().split()))
n_arr.sort()
for num in m_arr:
    found = False
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if num == n_arr[mid]:
            found = True
            break
        elif num < n_arr[mid]:
            end = mid - 1
        elif num > n_arr[mid]:
            start = mid + 1

    if not found:
        print(0)
    else:
        print(1)

