import math
def solution(number, limit, power):
    total = 0
    for i in range(1, number + 1):
        count = 0
        if i == 1:
            count = 1
        else:
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    if i // j == j:
                        count += 1
                    else:
                        count += 2
        if count > limit:
            count = power
        total += count
    print(total)

def commonFactor(n):
    commonFactors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            commonFactors.append(n // i)
            commonFactors.append(i)
        return len(set(commonFactors))

def solution2(number, limit, power):
    return sum([commonFactor(i) if commonFactor(i) <= limit else power for i in range(1, number + 1)])

solution(10, 3, 2)

