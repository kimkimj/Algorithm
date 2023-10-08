def solution(numbers):

    stack = []
    ans = [-1] * len(numbers)
    for i in range(len(numbers)):
        current = numbers[i]
        to_be_removed = []
        for index in stack:
            if current > numbers[index]:
                ans[index] = current
                to_be_removed.append(index)
        for n in to_be_removed:
            stack.remove(n)

        stack.append(i)

    return ans

numbers = [2, 3, 3, 5]
print(solution(numbers))

# for each loop는 사실 index에 기반으로 돌아가기 때문에,
# for index in stack을 했을 때, 즉 for each loop을 도는 객체의
# 사이즈가 줄면 for loop도 조기 종영될 수 있다...
# index가 1이였는데 stack의 사이즈가 1임..