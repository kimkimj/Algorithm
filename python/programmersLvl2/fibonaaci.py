def solution(n):
    prev_1 = 0
    prev_2 = 1

    for i in range(n - 1):
        temp = prev_2
        prev_2 = prev_1 + prev_2
        prev_1 = temp

    return prev_2 % 1234567

def solution2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# n은 100,000 이하이기 때문에 1234567보다 훨씬 작고 그렇기 때문에 굳이 이 숫자로 나눌 필요가 없다

print(solution(5))



