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
solution(10, 3, 2)

