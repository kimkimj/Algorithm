def solution(order):
    prev = order[0] + 1
    count = 0
    for o in order:
        if o != prev - 1:
            break
        else:
            count += 1
            prev = o
    return count

order = [1, 2, 3]
print(solution(order))