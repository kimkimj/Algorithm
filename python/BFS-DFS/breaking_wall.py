import sys
from collections import deque

def bfs(wall_r, wall_c, maze):
    maze[wall_r][wall_c] = 0
    queue = deque([(0, 0)])
    visited = [[-1] * columns for _ in range(rows)]
    visited[0][0] = 1

    while queue:
        r, c = queue.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < columns \
                and maze[nr][nc] == 0 and visited[nr][nc] == -1:

                queue.append((nr, nc))
                # count += 1 이렇게 하면 방문한 모든 vertices를 count하게 된다
                # 방문한 level을 count해야 하기 때문에
                # count = maze[r][c] + 1 이렇게하면 0과 1 하나에 1을 더한 결과를 반환
                visited[nr][nc] = visited[r][c] + 1
    #the function did not make a copy of the 2d array, but referenced to it
    # the change made by the function applies to the original reference
    maze[wall_r][wall_c] = 1
    return visited[rows - 1][columns - 1]

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

# too many syntax errors that do not result in exceptions, but unexpected results
# visited = ... instead of visted[][]
# visted[][] == 1 instead of visited[][] = ..