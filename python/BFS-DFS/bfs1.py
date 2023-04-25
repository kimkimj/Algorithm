import sys
from collections import deque
input = sys.stdin.readline

def bfs(V, E, start):
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(V + 1):
        graph[i].sort()

    visited = [-1] * (V + 1)
    order = [0] * (V + 1)
    queue = deque([start])
    count = 1
    while queue:
        current = queue.popleft()
        if visited[current] == -1:
            visited[current] = 1
            order[current] = count
            count += 1

            for adjacent in graph[current]:
                if visited[adjacent] != 1:
                    queue.append(adjacent)

    print(*order[1:], sep="\n")

v, e, start = map(int, input().split())
bfs(v, e, start)