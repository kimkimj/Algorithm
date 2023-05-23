
def floyd_warshall():
    INF = float('inf')
    V, E = map(int, input().split())

    dist = [[INF] * V for _ in range(V)]
    for i in range(V):
        dist[i][i] = 0

    for _ in range(E):
        s, d, w = map(int, input().split())
        dist[s][d] = w

    for m in range(V):
        for s in range(V):
            for t in range(V):
                dist[s][t] = min(dist[s][t], dist[s][m] + dist[t][m])

    for i in range(V):
        if dist[i][i] < 0:
            return -1
    return dist

print(floyd_warshall())