from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
rows, columns = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(rows)]
visited = [[0] * columns for _ in range(rows)]
dist = [[0] * columns for _ in range(rows)]
queue = deque()
for r in range(rows):
    for c in range(columns):
        if graph[r][c] == 1 and visited[r][c] == 0:
            count = 1
            queue.append((r, c))
            visited[r][c] = 1
            dist[r][c] = count

            while queue:
                current_r, current_c = queue.popleft()

                for dr, dc in delta:
                    nr = current_r + dr
                    nc = current_c + dc

                    if 0 <= nr < rows and 0 <= nc < columns and \
                        graph[nr][nc] == 1 and visited[nr][nc] == 0:
                        queue.append((nr, nc))
                        visited[nr][nc] = 1
                        count = dist[current_r][current_c] + 1
                        if dist[nr][nc] == 0:
                            dist[nr][nc] = count
                        else:
                            dist[nr][nc] = min(dist[nr][nc], count)

print(dist[rows - 1][columns - 1])


