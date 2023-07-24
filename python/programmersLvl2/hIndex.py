def solution(citations):
    answer = 0
    start = 0
    end = max(citations)

    while start <= end:
        mid = (start + end) // 2

        count = 0
        for paper in citations:
            if paper >= mid:
                count += 1

        if count >= mid:
            start = mid + 1
            answer = mid

        else: # mid < count
            end = mid - 1

    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))