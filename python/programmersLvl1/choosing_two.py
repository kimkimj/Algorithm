def solution(numbers):
    arr = set()
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            arr.add(numbers[i] + numbers[j])

    arr = list(arr)
    return arr.sort()

solution([2,1,3,4,1])
solution([5,0,2,7])