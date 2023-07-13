num_tteok, min_height = 4, 6
arr = [19, 15, 10, 17]

start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for h in arr:
        if h > mid:
            total += h - mid
    if total > min_height:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)




