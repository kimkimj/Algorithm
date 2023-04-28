from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())

for i in range(t):
    col, row, v = map(int, input().split())
    farm = [[0] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    for _ in range(v):
        x, y = map(int, input().split())
        farm[x][y] = 1

    queue = deque()
    count = 0
    for r in range(row):
        for c in range(col):
            if farm[r][c] == 1 and visited[r][c] == 0:
                queue.append((x, y))
                farm[x][y] = 1
                count = 1

            while queue:
                x, y = queue.popleft()

                for dx, dy in dx, dy:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < col and 0 <= ny < row and \
                        farm[nx][ny] == 1 and visited[nx][ny] == 0:
                        queue.append((nx, ny))


