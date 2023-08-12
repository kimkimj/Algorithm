from collections import deque
def solution(numbers, target):
    count = 0
    que = deque([(numbers[0], 1), (-numbers[0], 1)])
    i = 1
    while que:
        current, i = que.popleft()
        if i == len(numbers) - 1:
            if current + numbers[i] == target:
                count += 1
            elif current - numbers[i] == target:
                count += 1
        else:
            que.append((current + numbers[i], i + 1))
            que.append((current - numbers[i], i + 1))
    return count

numbers =[1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))