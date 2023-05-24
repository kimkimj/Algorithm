from collections import deque
def solution(n):
    queue = deque([])
    while n > 0:
        queue.append(n % 3)
        n = n // 3

    num = 0
    count = 0
    while queue:
        num += queue.pop() * pow(3, count)
        count += 1
    return num

print(solution(45))
