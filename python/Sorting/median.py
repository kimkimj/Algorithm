arr = []
for i in range(5):
    arr.append(int(input()))

average = sum(arr) // 5
print(average)

# array must be sorted first
arr.sort()
median = arr[2]
print(median)
