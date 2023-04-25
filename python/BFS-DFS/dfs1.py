v, e, start = map(int, input().split())
graph = [[] for _ in range(e)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort(reverse=True)

count = 1
stack = [start]
visited = [-1] * (v + 1)
order = [0] * (v + 1)
while stack:
    current = stack.pop()
    if visited[current] == -1:
        visited[current] = 1
        order[current] = count
        count += 1

        for adjacent in graph[current]:
            if visited[adjacent] == -1:
                stack.append(adjacent)

print(*order[1:], sep = "\n")
