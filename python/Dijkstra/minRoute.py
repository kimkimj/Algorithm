import sys
import heapq

INF = float('inf')
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

min_dist = [INF] * (V + 1)
que = [(0, start)] # weight determines the priority
min_dist[start] = 0
while que:
    current_weight, current = heapq.heappop(que)

    for adjacent, adjacent_weight in graph[current]:

        # check if the distance to the neighboring node through this node is shorter
        new_weight = current_weight + adjacent_weight
        if new_weight < min_dist[adjacent]:
            min_dist[adjacent] = new_weight
            que.append((new_weight, adjacent))

for i in range(1, V + 1):
    if min_dist[i] == INF:
        print('INF')
    else:
        print(min_dist[i])