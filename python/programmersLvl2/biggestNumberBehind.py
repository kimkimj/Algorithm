def solution(numbers):

    stack = []
    ans = [-1] * len(numbers)
    for i in range(len(numbers)):
        current = numbers[i]
        while stack and current > numbers[stack[-1]]:
            if current > numbers[stack[-1]]:
                ans[stack.pop()] = current
        stack.append(i)

    return ans

numbers = [2, 5, 6, 3]
print(solution(numbers))

# how can this code assume that there is no number smaller than itself and thereby become a
# 뒤큰수 for another number when it encounters a bigger number???

# 현재 수는 stack을 iterate하다, 자신보다 큰 수가 있으면 멈춘다
# 왜냐하면 자신보다 큰 수가 스택에 있다면, 큰 수 아래에 있는 수의 "더 큰 수"가 되지 못했다는 뜻이다
# 즉 큰 수 보다 더 큰 수라는 뜻이다

# 3 4 3 2 1 3 을 생각해 보라
# stack에는 [3]이 먼저 들어가지만 4에 의해 제거된다. (key point)
# 그 후로는 [4, 3, 2, 1]이 들어가고 3에 의해 [4, 3]만 남게 된다.
# 현재 후인 3으로 제거될 수 있는 수들은 4로 인해 벌써 제가된 상태이다
