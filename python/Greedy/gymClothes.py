n =3
lost = [3]
reserve = [1]

def solution(n, lost, reserve):
    count = n - len(lost)
    arr = [False] * n
    for i in range(len(reserve)):
        arr[reserve[i] - 1] = True

    for i in range(len(lost)):
        if lost[i] - 2 >= 0 and arr[lost[i] - 2]:
            count += 1
            arr[lost[i] - 2] = False
        elif lost[i] + 2 < len(arr) and arr[lost[i] + 2]:
            count += 1
            arr[lost[i] + 2] = False

    print(count)