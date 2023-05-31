def solution(n, m, section):
    total = 0
    index = 0
    while index < len(section):
        for i in range(section[index], section[index] + m):
            if i in section[index:]:
                index += 1
        total += 1
    return total

print(solution(4, 1, [1, 2, 3, 4]))