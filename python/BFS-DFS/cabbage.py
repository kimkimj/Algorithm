
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n = int(input())

for i in range(n):
    columns, rows, v = map(int, input().split())
    farm = [[0] * columns for _ in range(rows)]
    for j in range(v):
        x, y = map(int, input().split())
        farm[y][x] = 1

    visited = [[0] * columns for _ in range(rows)]
    stack = []
    count = 0
    for r in range(rows):
        for c in range(columns):
            if farm[r][c] == 1 and visited[r][c] == 0:
                stack.append((r, c))
                visited[r][c] = 1
                count += 1

                while stack:
                    current_r, current_c = stack.pop()

                    for dc, dr in delta:
                        nr = current_r + dr
                        nc = current_c + dc

                        if 0 <= nr < rows and 0 <= nc < columns and \
                                farm[nr][nc] == 1 and visited[nr][nc] == 0:
                            stack.append((nr, nc))
                            visited[nr][nc] = 1
    print(count)



