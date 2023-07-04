def solution(ingredient):
    stack = []
    count = 0
    for i in range( len(ingredient)):
        stack.append(ingredient[i])

        # stack[-4] == 1231 하면 틀리다. stack의 sub array를 가져오는 것이고, 그게 array이기 때문에
        # if ingredient[i] == 1 and stack[-4:] == [1, 2, 3, 1]:
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            count += 1
    return count

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))