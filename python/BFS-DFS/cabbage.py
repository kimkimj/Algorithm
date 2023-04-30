from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())

for i in range(n):
    col, row, v = map(int, input().split())

    farm = [[0] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    for _ in range(v):
        x, y = map(int, input().split())
        farm[y][x] = 1

    queue = deque()
    count = 0

    for r in range(row):
        for c in range(col):
            if farm[r][c] == 1 and visited[r][c] == 0:
                queue.append((c, r)) # c = x, r = y
                visited[r][c] = 1
                count += 1

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < col and 0 <= ny < row and \
                            farm[ny][nx] == 1 and visited[ny][nx] == 0:

                            visited[ny][nx] = 1
                            queue.append((nx, ny))
    print(count)

