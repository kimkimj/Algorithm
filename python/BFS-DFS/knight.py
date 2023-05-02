import sys
from collections import deque

input = sys.stdin.readline
#y, x
delta = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2)]

cases = int(input())
for _ in range(cases):
    length = int(input())
    start_x, start_y = list(map(int, input().split())) # x, y
    target_x, target_y = list(map(int, input().split())) # x, y

    queue = deque()
    queue.append([start_x, start_y])
    visited = [[-1] * length for _ in range(length)]
    visited[start_y][start_x] = 0
    count = 0

    while queue:
        x, y = queue.popleft()

        for i in range(len(delta)):
            dy, dx = delta[i]
            ny = y + dy
            nx = x + dx

            if 0 <= nx < length and 0 <= ny < length and \
                visited[ny][nx] == -1:
                queue.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1
                if ny == target_y and nx == target_x:
                    queue = deque() #break out of the while loop
                    break
    print(visited[target_y][target_x])




