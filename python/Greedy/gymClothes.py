def solution(n, lost, reserve):
    count = n - len(lost)
    arr = [False] * n

    for index in reserve:
        arr[index - 1] = True

    newLost = []
    # 체육복을 잃어버렸지만 여유분이 있을 때
    lost.sort()
    for index in lost:
        if arr[index - 1]:
            arr[index - 1] = False
            count += 1
        else:
            newLost.append(index - 1)

    for index in newLost:
        if index - 1 > -1 and arr[index - 1]:
            arr[index - 1] = False
            count += 1
        elif index + 1 < len(arr) and arr[index + 1]:
            arr[index + 1] = False
            count += 1
    print(count)


n = 5
lost = [4, 2]
reserve = [3, 5]

solution(n ,lost ,reserve)