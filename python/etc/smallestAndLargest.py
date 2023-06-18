def solution(s):
    arr = list(map(int, s.split(' ')))
    max, min = arr[0], arr[0] # -100 100
    for num in arr:
        if num > max:
            max = num
        elif num < min:
            min = num
    return str(min) + ' ' + str(max)

def solution2(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + ' ' + str(max(arr))

s = "5 8 2 7 4 3"
print(solution(s))