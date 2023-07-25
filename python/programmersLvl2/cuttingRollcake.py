def solution(topping):
    sliceA = {}
    sliceB = {}
    count = 0

    #sliceB 에 다 넣기
    for t in topping:
        if t in sliceB:
            sliceB[t] += 1

        else:
            sliceB[t] = 1

    for i in range(len(topping)):
        t = topping[i]

        if t in sliceA:
            sliceA[t] += 1

        else:
            sliceA[t] = 1

        # remove the newly added topping from slice B:
        sliceB[t] -= 1
        if sliceB[t] == 0:
            del sliceB[t]

        if len(sliceA) == len(sliceB):
            count += 1

    return count

topping = [1, 2, 3, 1, 4]
print(solution(topping))




