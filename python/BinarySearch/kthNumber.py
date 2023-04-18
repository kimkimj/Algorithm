n = int(input())
k = int(input())

arr = [0] * (n * n)
count = 0
for row in range(1, n + 1):
    for column in range(1, n + 1):
        arr[count] = row * column
        count += 1

arr.sort()
print(arr[k - 1])


