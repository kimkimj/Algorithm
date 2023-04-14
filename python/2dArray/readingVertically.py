arr = []
length = 0
for i in range(5):
    arr.append(input())
    length = max(length, len(arr[i]))

line = ""
for j in range(length):
    for row in range(5):
        if j < len(arr[row]):
            line += arr[row][j]
print(line)