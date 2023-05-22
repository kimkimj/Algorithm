
def solution(n):
    # 2부터 n까지의 수가 포함된 set
    numbers = set(range(2, n + 1))

    # iterate through every number in the set
    for i in range(2, n + 1):
        if i in numbers:
            numbers -= set(range(2 * i, n + 2, i))
    return len(numbers)



print(solution(5))

# https://www.acmicpc.net/board/view/39203
# https://hwan-hobby.tistory.com/108