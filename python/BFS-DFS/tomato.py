import sys
from collections import deque

input = sys.stdin.readline
def bfs():
    col, row = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(row)]

    queue = deque()
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(row):
        for c in range(col):
            visited = [[0] * col for _ in range(row)]
            if box[r][c] == 1 and visited[r][c] == 0:
                queue.append([r, c])
                visited[r][c] = 1

                while queue:
                    current_r, current_c = queue.popleft()
                    for k in range(4):
                        dr, dc = delta[k]
                        nr = current_r + dr
                        nc = current_c + dc

                        if 0 <= nr < row and 0 <= nc < col and \
                            visited[nr][nc] == 0:

                            if box[nr][nc] >= 0:
                                queue.append([nr, nc])

                                if box[nr][nc] == 0:
                                    box[nr][nc] = box[current_r][current_c] + 1
                                else: # box > 0
                                    box[nr][nc] = min(box[nr][nc], box[current_r][current_c] + 1)
                            visited[nr][nc] = 1

    total_days = 0
    for r in range(row):
        for c in range(col):
            if box[r][c] == 0:
                return -1
            total_days = max(total_days, box[r][c])
    return total_days - 1

print(bfs())

#https://velog.io/@hysong/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
