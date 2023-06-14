from collections import deque
def solution(maps):
    answer = 0
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    delta = [(0,1), (0, -1), (1,0), (-1, 0)]
    que = deque([(0, 0)])
    while que:
        current_r, current_c = que.popleft()
        for dr, dc in delta:
            nr = current_r + dr
            nc = current_c + dc

            if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]):
                if maps[nr][nc] == 1 and visited[nr][nc] == 0:
                    que.append((nr, nc))
                    visited[nr][nc] = visited[current_r][current_c] + 1
    last_row = len(maps) - 1
    last_column = len(maps[0]) - 1
    if visited[last_row][last_column] == 0:
        return -1
    else:
        return visited[last_row][last_column]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))


