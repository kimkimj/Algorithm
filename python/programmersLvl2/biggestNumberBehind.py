def solution(numbers):

    stack = []
    ans = [-1] * len(numbers)
    for i in range(len(numbers)):
        current = numbers[i]
        to_be_removed = []
        while stack and stack[-1]
            if current > numbers[index]:
                ans[index] = current
                to_be_removed.append(index)


        stack.append(i)

    return ans

numbers = [2, 3, 3, 5]
print(solution(numbers))

