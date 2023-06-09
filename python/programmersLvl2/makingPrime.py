from itertools import permutations
import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    #l = list(map(int, numbers.split(''))) -> ValueError: empty separator
    numbers = list(map(int, list(numbers)))
    count = 0
    for i in range(1, len(numbers) + 1):
        perm = permutations([numbers], i)
        number = ''
        for combo in list(perm):
            for c in list(combo):
                number += c
        number = int(number)
        if isPrime(number):
            count += 1
    return count

def solution2(numbers):
    arr = permutations(numbers)
    arr = list(arr)
    for combo in arr:
        print(combo)

print(solution2(17))