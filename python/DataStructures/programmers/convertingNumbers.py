import math

def solution(x, y, n):
    answer = math.inf
    if (y - x) % n == 0:
        answer = min(answer, int((y - x) / n))
    if (math.log(y / x) / math.log(2)).is_integer():
        answer = min(answer, int(math.log(y / x) / math.log(2)))
    if (math.log(y / x) / math.log(3)).is_integer():
        answer = min(answer, int(math.log(y / x) / math.log(3)))

    if answer == math.inf:
        while n <= y:


    if answer != math.inf:
        return answer
    else:
        return -1

if __name__ == '__main__':
    print(solution(10, 40, 5))