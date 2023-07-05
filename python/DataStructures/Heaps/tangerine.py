import heapq
def solution(k, tangerine):
    answer = 0
    sizes = {}
    for num in tangerine:
        if num not in sizes:
            sizes[num] = 1
        else:
            sizes[num] = sizes[num] + 1

    heap = []
    for key in sizes:
        occ = sizes[key]
        heapq.heappush(heap, (-occ, key))

    count = 0
    while count < k:
        count += -heapq.heappop(heap)[0]
        answer += 1

    return answer

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
print(solution(k, tangerine))