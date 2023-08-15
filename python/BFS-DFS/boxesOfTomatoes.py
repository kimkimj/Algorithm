import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

def bfs():
    directions = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]
    que = deque()

    # 처음부터 익은 토마토 que에 담기
    for box in range(h):
        for row in range(n):
            for col in range(m):
                if tomatoes[box][row][col] == 1:
                    que.append((box, row, col))


    # 처음부터 익은 토마토 주변에 있는 토마토들을 넣고, 다른 처음부터 익은 토마토의 주변을 탐색한다
    # 이렇게 하면 주변 토마토를  탐색할 때 아직 익지않은 토마토만 탐색해도 된다
    # 이미 익은 토마토는 at its minimum
    while que:
        current_box, current_row, current_col = que.popleft()

        for nh, nr, nc in directions:
            new_box = current_box + nh
            new_row = current_row + nr
            new_col = current_col + nc

            # 익지 않은 토마토들만 익게 한다
            if (0 <= new_box < h) and (0 <= new_row < n) and (0 <= new_col < m) \
                    and tomatoes[new_box][new_row][new_col] == 0:

                    tomatoes[new_box][new_row][new_col] = tomatoes[current_box][current_row][current_col] + 1
                    que.append((new_box, new_row, new_col))

    days = 0
    for box in tomatoes:
        for row in box:
            if 0 in row:
               return -1
            days = max(days, max(row))
    return days - 1

print(bfs())
