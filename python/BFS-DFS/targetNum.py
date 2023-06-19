def solution(numbers, target):
    graph = [0]
    count = 0

    for num in numbers:
        temp = []

        for node in graph:
            temp.append(node + num)
            temp.append(node - num)

        graph = temp

    for leaf in graph:
        if leaf == target:
            count += 1
    return count

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))