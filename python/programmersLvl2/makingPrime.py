from itertools import permutations
import math

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    #l = list(map(int, numbers.split(''))) -> ValueError: empty separator
    temp = []
    for i in range(1, len(numbers) + 1):
        temp += list(permutations(numbers, i))

    unique_numbers = set()
    count = 0
    for t in temp:
        num = int(''.join(t))
        if num not in unique_numbers:
            unique_numbers.add(num)
            if is_prime(num):
                count += 1
    return count

print(solution("011"))