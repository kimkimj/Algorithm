from collections import deque
def solution(n, computers):

    graph = [[] for _ in range(n)]

    que = deque()
    visited = [0] * n
    count = 0
    for i in range(len(computers)):
        if visited[i] == 0:
            count += 1
            que.append(i)
            visited[i] = 1

            while que:
                current = que.popleft()
                for j in range(len(computers[0])):
                    if computers[current][j] == 1 and visited[j] == 0:
                        visited[j] = 1
                        que.append(j)

    return count

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))


