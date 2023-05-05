from collections import deque


n = int(input())
apt = [list(map(int, list(input()))) for _ in range(n)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = []

queue = deque([(0, 0)])
for r in range(n):
    for c in range(n):
        if apt[r][c] == 1:
            count = 1
            queue.append((r, c))
            apt[r][c] = 0

            while queue:
                y, x = queue.popleft()

                for dx, dy in delta:
                    ny = y + dy
                    nx = x + dx

                    if 0 <= nx < n and 0 <= ny < n and \
                        apt[ny][nx] == 1:
                        queue.append((ny, nx))
                        apt[ny][nx] = 0
                        count += 1

            answer.append(count)
print(len(answer))
answer.sort()
print(*answer, sep="\n")