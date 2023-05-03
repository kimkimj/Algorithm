import sys
from collections import deque

def bfs(wall_r, wall_c, maze):
    maze[wall_r][wall_c] = 0
    queue = deque([(0, 0)])
    visited = [[-1] * columns for _ in range(rows)]
    visited[0][0] = 1
    count = 1

    while queue:
        r, c = queue.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < columns \
                and maze[nr][nc] == 0 and visited == -1:
                visited[nr][nc] == 0
                queue.append((nr, nc))
                count += 1
                if nr == rows - 1 and nc == columns - 1:
                    return count
    return -1

rows, columns = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(rows)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

shortest = columns * rows
for y in range(rows):
    for x in range(columns):
        if (y == 0 and x == 0) or maze[y][x] == 1:
            num_path = bfs(y, x, maze)
            if num_path != -1:
                shortest = min(shortest, num_path)
if shortest == columns * rows:
    print(-1)
else:
    print(shortest)
