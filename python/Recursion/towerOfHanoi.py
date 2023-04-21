def hanoi(num, start, end):
    if num == 1:
        print(start, end)
    else:
        hanoi(num - 1, start, 6 - start - end)
        print(start, end)
        hanoi(num - 1, 6 - start - end, end)

num = int(input())
print(2 ** num - 1)
hanoi(num, 1, 3)