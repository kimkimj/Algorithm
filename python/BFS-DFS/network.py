from collections import deque
def solution(n, computers):

    graph = [[] for _ in range(n)]

    for row in range(len(computers)):
        for col in range(len(computers[0])):
            if computers[row][col] == 1 and row != col:
                graph[row].append(col)

    que = deque()
    visited = [0] * n
    count = 0
    for i in range(len(graph)):
        if visited[i] == 0:
            count += 1
            que.append(i)
            visited[i] = 1

            while que:
                current = que.popleft()
                for neighbor in graph[current]:
                    if visited[neighbor] == 0:
                        visited[neighbor] = 1
                        que.append(neighbor)

    return count

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))


