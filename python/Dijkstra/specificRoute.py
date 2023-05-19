import sys
import heapq

input = sys.stdin.readline
INF = float('inf')
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))
v1, v2 = map(int, input().split())

def dijakstra(start):
    min_dist = [INF] * (V + 1)
    min_dist[start] = 0
    queue = [(0, start)]
    while queue:
        current_dist, current = heapq.heappop(queue)

        for distance_to_adjacent, adjacent in graph[current]:
            new_dist = current_dist + distance_to_adjacent

            if new_dist < min_dist[adjacent]:
                min_dist[adjacent] = new_dist
                heapq.heappush(queue, (new_dist, adjacent))
    return min_dist

one = dijakstra(1)
v_one = dijakstra(v1)
v_two = dijakstra(v2)

path1 = one[v1] + v_one[v2] + v_two[V]
path2 = one[v2] + v_two[v1] + v_one[V]
answer = min(path1, path2)

if answer == INF:
    print(-1)
else:
    print(answer)
