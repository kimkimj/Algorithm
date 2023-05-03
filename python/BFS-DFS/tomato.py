import sys
from collections import deque

input = sys.stdin.readline

columns, rows = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(rows)]

def bfs():
    queue = deque()

    # Iterate through the 2d array and place the cells with 1 in a queue
    # 이렇게 하면 1로 시작하는 cell을 한번씩 돌면서 1에서 가까운 cell들 먼저 돌게 된다
    # bfs in multiple locations
    for r in range(rows):
        for c in range(columns):
            if box[r][c] == 1:
                queue.append((r, c))

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < columns and \
                box[nr][nc] == 0:
                queue.append((nr, nc))
                box[nr][nc] = box[r][c] + 1

    total_days = 0
    for r in range(rows):
        for c in range(columns):
            if  box[r][c] == 0:
                return -1
            total_days = max(total_days, box[r][c])
    return total_days - 1

print(bfs())