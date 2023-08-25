from collections import deque

t = int(input())
for _ in range(t):
    graph = {}
    visited = {}

    num_conv = int(input())
    home = tuple(map(int, input().split()))
    graph[home] = []
    visited[home] = True

    for i in range(num_conv + 1):
        x, y = map(int, input().split())
        if i == num_conv:
            festival = (x, y)
        graph[(x, y)] = []
        visited[(x, y)] = False

        for x1, y1 in graph:
            dist = abs(x - x1) + abs(y - y1)
            if 0 < dist <= 1000:
                graph[(x1, y1)].append((x, y))
                graph[(x, y)].append((x1, y1))

    answer = False
    que = deque([(home)])
    while que:
        current = que.popleft()

        for neighbor in graph[current]:
            if neighbor == festival:
                answer = True
                break
            if visited[neighbor] == False:
                visited[neighbor] = True
                que.append(neighbor)

    if answer:
        print("happy")
    else:
        print("sad")


