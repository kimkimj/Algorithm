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
    graph[i].sort()

# deque를 사용하지 않고 list를 사용하면 시간초과
queue = deque([start])
order = [0] * (V + 1)
visited = [-1] * (V + 1)
count = 1
while queue:
    current = queue.popleft()
    # if visited[adjacent]로 방문하지 않은 node만 더하지만 adjacent nodes 끼리 share 하는
    # neighbor가 있으면 중복으로 담기기 때문에 여기서 한번 더 확인해야한다
    if visited[current] == -1:
        visited[current] = 1
        order[current] = count
        count += 1

        for adjacent in graph[current]:
            if visited[adjacent] == -1:
                queue.append(adjacent)

print(*order[1:], sep="\n")