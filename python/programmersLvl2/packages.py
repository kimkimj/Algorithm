from collections import deque

def solution(order):
    order = deque(order)
    count = 0
    stack = []

    for i in range(1, len(order) + 1):
        if i == order[0]:
            order.popleft()
            count += 1
            while len(stack) > 0 and order[0] == stack[-1]:
                order.popleft()
                stack.pop()
                count += 1
        else:
            stack.append(i)
    return count


order = [1,2,4,5,3,6]
print(solution(order))