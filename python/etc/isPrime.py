def is_prime(num):
    if num == 1:
        return False
    divisor = [2, 3, 5, 7]
    for i in range(len(divisor)):
        if num != divisor[i] and num % divisor[i] == 0:
            return False
    return True
def solution(n):
    count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            count += 1
    return count

print(solution(11))

# https://www.acmicpc.net/board/view/39203