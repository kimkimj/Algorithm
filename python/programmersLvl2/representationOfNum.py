def solution(n):
    count = 1 # the number itself
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            consec = list(range(i, j + 1))
            total = sum(consec)
            if total == n:
                count += 1
            elif total > n:
                break
    return count

print(solution(15))

