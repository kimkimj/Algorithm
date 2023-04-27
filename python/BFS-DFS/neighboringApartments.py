from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
homes = [list(map(int, list(input().strip()))) for _ in range(n)]
counts = [0]
visited = [[0] * n for _ in range(n)]

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# (-1, 0) left, (1, 0) right, (0, -1) above, (0, 1) below

for i in range(n):
    for j in range(n):
        # if the apartment exists, but has not been visited
        if homes[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            queue.append([i, j])
            visited[i][j] = 1
            while queue:
                x, y = queue.popleft()

                # explore all four adjacent cells
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    # if the neighboring cell has not been visited and
                    # there IS an apartment at the location
                    if 0 <= nx < n and 0 <= ny < n and \
                             homes[nx][ny] != 0 and visited[nx][ny] == 0:

                        # mark the apartment as visited
                        # add it to the queue
                        # add to the count
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                        cnt += 1

            # when the queue ends, bfs has ended
            # no more connected cells
            counts.append(cnt)

print(len(counts) - 1)
counts.sort()
print(*counts[1:], sep='\n')






