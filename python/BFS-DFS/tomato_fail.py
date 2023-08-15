import sys
from collections import deque

input = sys.stdin.readline

m, n= map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
que = deque([])
for r in range(n):
    for c in range(m):

        if tomatoes[r][c] == 1:
            que.append((r, c))

            while que:
                current_r, current_c = que.popleft()

                for dr, dc in directions:
                    nr = current_r + dr
                    nc = current_c + dc

                    if (0 <= nr < n) and (0 <= nc < m) and tomatoes[nr][nc] != -1:
                        if tomatoes[nr][nc] != 0:
                            tomatoes[nr][nc] = min(tomatoes[current_r][current_c] + 1, tomatoes[nr][nc])
                        else:
                            tomatoes[nr][nc] = tomatoes[current_r][current_c] + 1
                            que.append((nr, nc))

days = -1
for r in range(n):
    for c in range(m):
        if tomatoes[r][c] == 0:
            print(-1)
            exit()
        else:
            days = max(days, tomatoes[r][c])
print(days - 1)