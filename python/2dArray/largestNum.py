arr = []
for i in range(9):
    row = list(map(int, input().split()))
    arr.append(row)

max = arr[0][0]
max_index = [0, 0]
for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]
            max_index = [i, j]
print(max)
print(max_index[0] + 1, max_index[1] + 1)
