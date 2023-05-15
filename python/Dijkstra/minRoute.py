import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
start = int(input())

# 비용을 무한대로 초기화
min_dist = [INF] * (V + 1)

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

que = []
heapq.heappush(que, (0, start)) #minimum distance to the node, node
# 시작 node의 비용은 0
min_dist[start] = 0
while que:
    current_weight, current = heapq.heappop(que)

    for adjacent, adjacent_weight in graph[current]:
        new_w = current_weight + adjacent_weight

        if new_w < min_dist[adjacent]:
            min_dist[adjacent] = new_w
            heapq.heappush(que, (new_w, adjacent))

for i in range(1, V + 1):
    if min_dist[i] == INF:
        print('INF')
    else:
        print(min_dist[i])