def merge_sort(arr):
    if len(arr) < 2:
        return arr // 2
    mid = len(arr) // 2
    left_half, count = merge_sort(arr[:mid])
    right_half, count = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(left_half) and h < len(right_half):
        saved = 0
        if left_half[l] < right_half[h]:
            saved = left_half[l]
            merged_arr.append(left_half[l])
            l += 1
        else:
            saved = right_half[h]
            merged_arr.append(right_half[h])
            h += 1

    merged_arr += left_half[l:]
    merged_arr += right_half[h:]
    return merged_arr, count

merge_sort([4, 5, 1, 3, 2])