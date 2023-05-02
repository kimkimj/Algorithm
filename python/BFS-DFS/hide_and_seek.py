from collections import deque

n, k = map(int, input().split())
#graph = [-1] * max(n + 1, k + 1)
graph = [-1] * 100001
queue = deque([n])
graph[n] = 0
while queue:
    index = queue.popleft()
    #delta = [-1, 1, index]
    #for i in range(3):
    #    nx = index + delta[i]
    for i in (index + 1, index - 1, index * 2):
        if 0 <= nx < len(graph) and graph[nx] == -1:
            #nx = index + delta[i]
            nx = index + i
            graph[nx] = graph[index] + 1
            if nx == k:
                break
            queue.append(nx)

print(graph[k])
