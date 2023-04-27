import sys
from collections import deque

input = sys.stdin.readline
V, E, start = map(int, input().split())

graph = [[] for _ in range(V + 1)]

for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(V + 1):
    graph[i].sort(reverse=True)


visited = [0] * (V + 1)
order = [0] * (V + 1)
queue = deque([start])
count = 1
while queue:
    current = queue.popleft()
    if visited[current] == 0:
        visited[current] = 1
        order[current] = count
        count += 1

        # explore neighboring nodes if they have not been visited
        for adjacent in graph[current]:
            if visited[adjacent] == 0:
                queue.append(adjacent)
print(*order[1:], sep="\n")