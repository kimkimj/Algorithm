import sys
from collections import deque

input = sys.stdin.readline

V = int(input())
E = int(input())

# V + 1의 index를 만들어 줌으로서 index = 컴퓨터 번호를 뜻하게 한다
graph = [[] for _ in range(V + 1)]
for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [-1] * (V + 1)
queue = deque([1])

while queue:
    current = queue.popleft()
    if visited[current] == -1:
        count += 1
        visited[current] = 1

        for adjacent in graph[current]:
            if visited[adjacent] == -1:
                queue.append(adjacent)

# 1번 컴퓨터는 count에서 제외된다
print(count - 1)