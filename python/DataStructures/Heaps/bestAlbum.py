n = int(input())
v = int(input())

graph = [[] for i in range(n+1)] # 그래프 초기화
for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [0] * (n + 1)
def bfs(start):
    visited[start] = 1


            




