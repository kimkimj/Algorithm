import sys
from collections import deque

input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
parents = [0] * (V + 1)
parents[1] = 1

while queue:
    current = queue.popleft()

    for adjacent in graph[current]:
        if parents[adjacent] == 0:
            parents[adjacent] = current
            queue.append(adjacent)

print(*parents[2:], sep = "\n")