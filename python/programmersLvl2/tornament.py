import math
def solution(n,a,b):

    if a <= n // 2 and b > n //2 or b <= n// 2 and a > n// 2:

        return int(math.log(n, 2))

    else:
        group_a = int(a / 2)
        group_b = int(b / 2)

        #return int(math.log(abs(group_a - group_b), 2)) + 1
        prev = int(math.log(n, 2)) - 1
        prev = pow(2, prev)
        return int(math.log(prev, 2))

n = 16
a = 1
b = 7
print(solution(n, a, b))

