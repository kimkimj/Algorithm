import math

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n):
    count = 0
    for num in range(1, n + 1):
        if isPrime(num):
            count += 1
    return count

print(solution(10))