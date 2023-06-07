import math
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
numbers = map(int, input().split())
count = 0
for n in numbers:
    if is_prime(n):
        count += 1
print(count)