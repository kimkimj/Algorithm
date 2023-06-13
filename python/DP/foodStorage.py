def mySolution():
    n = 4
    storage = [1, 5, 10, 100]
    # 1 10 100
    # 1 5 10 100
    sum1, sum2 = 0, 0

    for i in range(len(storage)):
        if i % 2 == 0:
            sum2 += storage[i]
        else:
            sum1 += storage[i]

    print(max(sum1, sum2))

def dp():
    n = int(input())
    arr = list(map(int, input().split()))

    d = [0] * len(arr)
    d[0] = arr[0]
    d[1] = max(arr[0], d[1])

    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + arr[i])

    print(d[n - 1])