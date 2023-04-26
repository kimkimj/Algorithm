import sys
from collections import deque

input = sys.stdin.readline

V, E, start = map(int, input().split())
graph = [[] for _ in range(V + 1 )]
for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs():
    for i in range(V + 1):
        graph[i].sort(reverse=True)

    stack = [start]
    visited = [-1] * (V + 1)
    order = []

    while stack:
        current = stack.pop()
        if visited[current] == -1:
            visited[current] = 1
            order.append(current)

            for adjacent in graph[current]:
                if visited[adjacent] == -1:
                    stack.append(adjacent)
    print(*order)

def bfs():
    for i in range(V + 1):
        graph[i].sort()

    queue = deque([start])
    visited = [-1] * (V + 1)
    order = []

    while queue:
        current = queue.popleft()
        if visited[current] == -1:
            visited[current] = 1
            order.append(current)

            for adjacent in graph[current]:
                if visited[adjacent] == -1:
                    queue.append(adjacent)
    print(*order)

dfs()
bfs()