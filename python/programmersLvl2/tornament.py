import math
# https://eunhee-programming.tistory.com/145
def solution(n,a,b):
    answer = 0
    while True:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1
        if a == b:
            break
    return answer