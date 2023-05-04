import sys
from collections import deque

input = sys.stdin.readline
def bfs(start):
    queue = deque([start])
    colors[start] = 1

    while queue:
        current = queue.popleft()
        current_color = colors[current]

        for neighbor in graph[current]:
            if colors[neighbor] == 0:
                colors[neighbor] = current_color * - 1
                queue.append(neighbor)
            elif colors[neighbor] == current_color:
                return False
    return True

cases = int(input())
for _ in range(cases):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    colors = [0] * (v + 1) #0 unvisited, -1 red, 1 blue
    bipartite = True
    for i in range(1, v + 1):
        if colors[i] == 0:
            if not bfs(i): # bfs(i) == False
                bipartite = False
                break
    if bipartite:
        print("YES")
    else:
        print("NO")

# 그래프의 정점이 모두 연결된 경우만 생각했다.
# 연결되지 않는 두개의 그래프가 있을 때, 한 그래프가 BIPARTITE이 아니더라도 BIPARTITE인 그래프에서
# BFS를 시작하면 다른 그래프에 닻지 못하기 때문에 BIPARTITE이라는 잘못된 결과를 도출한다

# e.g.
# 1
# 5 4
# 1 2
# 3 4
# 3 5
# 4 5