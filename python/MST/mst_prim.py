import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, w  = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

visited = [-1] * (V + 1)
heap = [[0, 1]]
sum, count = 0, 0
while heap:
    weight, current = heapq.heappop(heap)

    if visited[current] == -1:
        visited[current] = 1
        sum += weight

        # neighhbor = [weight, vertex]
        for neighbor in graph[current]:
            heapq.heappush(heap, neighbor)

print(sum)


