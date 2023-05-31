def solution(n, m, section):
    total = 0
    index = 0
    while index < len(section):
        current = section[index]
        while index < len(section) and current <= section[index] <= current + m - 1:
            index += 1
        total += 1

    return total

def solution1(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1


print(solution(4, 1, [1, 2, 3, 4]))