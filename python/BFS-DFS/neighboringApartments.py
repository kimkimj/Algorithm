from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
homes = [list(map(int, list(input().strip()))) for _ in range(n)]
counts = [0]
visited = [[0] * n for _ in range(n)]

def bfs():
    vil_num = 1
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # (-1, 0) left, (1, 0) right, (0, -1) above, (0, 1) below

    for i in range(n):
        for j in range(n):
            # if the apartment has not been visited
            if homes[i][j] != 0 and visited[i][j] == 0:
                cnt = 0
                queue.append([i][j])
                visited[i][j] = vil_num
                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        # if the neighboring cell has not been visited and
                        # there is an apartment at the location
                        if 0 <= nx < n and 0 <= ny < n and \
                                visited[nx][ny] == 0 and homes[nx][ny] != 0:

                            # the neighboring apartment has the same vil_num as the current
                            visited[nx][ny] = vil_num
                            queue.append([nx, ny])
                            cnt += 1

                    counts.append(cnt)
                    vil_num += 1
    return vil_num - 1

vil_num = bfs()
counts.sort()
print(vil_num)
print(*counts[1:])





