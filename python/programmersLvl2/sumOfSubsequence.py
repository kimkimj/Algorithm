def solution(elements):
    answer = 0
    sums = []
    for length in range(1, len(elements) + 1):
        for i in range(len(elements)):

            end = i + length
            if end > len(elements):
                end = i + length - len(elements)
                num = sum(elements[i:len(elements)]) + sum(elements[:end])
                sums.append(num)
            else:
                num = sum(elements[i:end])
                sums.append(num)
    return len(set(sums))

elements =[7,9,1,1,4]
print(solution(elements))