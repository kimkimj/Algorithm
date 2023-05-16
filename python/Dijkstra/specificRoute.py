import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
v1, v2 = map(int, input().split())

# Start -> V1 -> V2 -> END
# START -> V2 -> V1 -> END
def dijkstra(start):
    que = [(0, start)]
    min_dist = [INF] * (V + 1)
    min_dist[start] = 0
    while que:
        current_weight, current = heapq.heappop(que)

        for adjacent, adjacent_weight in graph[current]:
            new_weight = current_weight + adjacent_weight
            if new_weight < min_dist[adjacent]:
                min_dist[adjacent] = new_weight
                que.append((new_weight, adjacent))
    return min_dist

one = dijkstra(1)
v1 = dijkstra(v1)
v2 = dijkstra(v2)

answer = min(one[v1] + v1[v2] + v2[V], one[v2] + v2[v1] + v1[V])

if answer < INF:
    print(answer)
else:
    print(-1)

