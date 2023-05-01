from collections import deque

n, k = map(int, input().split())
graph = [-1] * max(n + 1, k + 1)
queue = deque([n])
graph[n] = 0
while queue:
    index = queue.popleft()
    delta = [-1, 1, index]
    for i in range(3):
        nx = index + delta[i]
        if 0 <= nx < len(graph) and graph[nx] == -1:
            nx = index + delta[i]
            graph[nx] = graph[index] + 1
            if nx == n:
                break
            queue.append(nx)

print(graph[k])
