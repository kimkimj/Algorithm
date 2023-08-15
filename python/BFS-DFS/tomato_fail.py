# 풀이
#nested for loop로 익은 토마토 주면을 다 탐색 한 후, 다음으로 익은 토마토 주변을 탐색하면 실패한다.
# visited를 만든다 해도 익는 날까지의 minimum days를 구해야 하기 때문에 이미 익은 토마토도 다시 visit해야 하기 때문이다.
# 이 알고리즘은 설계가 잘못되어있다.

# 우선 박스를 돌면서 처음부터 익은 토마토를 que에 넣어야 한다.
# 그리고 while문을 돌며 bfs를 실행해야 한다
# 이렇게 되면 익은 토마토에서 한칸 떨어진 토마토들 부터 처리하게 된다

import sys
from collections import deque

input = sys.stdin.readline

columns, rows = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(rows)]

def bfs() :
    que = deque()

    for r in range(rows):
        for c in range(columns):
            if box[r][c] == 1:
                que.append((r, c))

    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while que:
        r, c = que.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < columns and box[nr][nc] == 0:
                box[nr][nc] = box[r][c] + 1
                que.append((nr, nc))

    total_days = 0
    for r in range(rows):
        for c in range(columns):
            if box[r][c] == 0:
                return -1
            else:
                total_days = max(total_days, box[r][c])
    return total_days - 1

print(bfs())