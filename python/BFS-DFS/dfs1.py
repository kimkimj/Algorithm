import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort(reverse=True)

def dfs(start):
    stack = [start]
    visited = [-1] * (N + 1)
    result = [0] * (N + 1)
    count = 1

    while stack:
        current = stack.pop()
        if visited[current] != 1:
            visited[current] = 1
            result[current] = count
            count += 1

            for adjacent in graph[current]:
                if visited[adjacent] == -1:
                    stack.append(adjacent)
    return result

result = dfs(R)
print(*result[1:], sep = '\n')
