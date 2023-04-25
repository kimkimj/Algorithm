def hanoi(num, start, end):

    if num == 1:
        print(start, end)
    else:
        # 1) num - 1개를 auxiliary rod로 이동
        hanoi(num - 1, start, 6 - start - end)

        # 2) 가장 큰 원반을 목표 rod로 이동
        print(start, end)

        #3) num - 1개를 auxilary rod에서 목표 rod로 이동
        hanoi(num - 1, 6 - start - end, end)

n = int(input)
print(2 ** n - 1)
hanoi(n, 1, 3)

#https://brenden.tistory.com/31