from itertools import combinations
import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
def solution(nums):
    count = 0
    for c in combinations(nums, 3):
        if isPrime(sum(c)):
            count += 1
    return count

print(solution([1,2,3,4]))