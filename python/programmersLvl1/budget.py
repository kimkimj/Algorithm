def solution(d, budget):
    # sorted RETURNS a sorted list, but does not modify the original
    d = sorted(d)
    # d.sort()

    count = 0
    # count must be bounded in case the total budget exceeds the budgets asked for
    while count < len(d) and budget - d[count] >= 0:
        budget -= d[count]
        count += 1

    return count

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))