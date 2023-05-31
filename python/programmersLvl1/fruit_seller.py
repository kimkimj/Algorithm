def solution(k, m, score):
    score.sort()
    sum = 0
    first_index = len(score) - m
    for _ in range(len(score) // m):
        sum += score[first_index] * m
        first_index -= m
    return sum

def solution2(k, m, score):
    score.sort(reverse = True)
    sum = 0
    # 그룹 중 가장 작은 숫자가 기준이 되기 때문에 m - 1에서 시작한다
    for i in range(m - 1, len(score), m):
        sum += score[i] * m
    return sum

print(solution2(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))