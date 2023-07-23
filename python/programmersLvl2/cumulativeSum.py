from collections import deque
def solution(elements):
    answer = []
    que = deque([])
    for length in range(1, len(elements) + 1):
        sum = 0
        for i in range(len(elements)):
            end = i + length
            if end >= len(elements):
                sum += sum(elements[:len(elements) - end])
            sum += elements[i]
            que.append(elements[i])
            if len(que) > length:
                sum -=  que.popleft()
            answer.append(sum)
    return set(answer)

elements = [7,9,1,1,4]
print(solution(elements))

