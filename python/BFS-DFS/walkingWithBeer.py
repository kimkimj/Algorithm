from collections import deque

def bfs():
    q = deque()
    q.append((home_x, home_y))
    while q:
        x, y = que.popleft()
        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            print("happy")
            return

        for i in range(n): #편의점들 확인
            if not visited[i]: #편의점을 방문하지 않음
                new_x, new_y = graph[i] # 새로운 편의점을 고르고
                if abs(x - new_x) + abs(y - new_y) <= 1000: # 현재 편의점에서 다음 거리까지 갈 수 있다면
                    visited[i] = 1
                    q.append((new_x, new_y))
    print("sad")
    return


t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    graph = []
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))

    festival_x, festival_y = map(int,input().split())
    visited = [0] * (n + 1)
    bfs()

# 편의점의 좌표를 받을 때, 거리가 1000 이하라면 서로의 neighbor로 등록했떤 지난번 코드와는 다르게
# 이 코드는 배열에 모든 편의점의 좌표를 등록하고 하나의 편의점에서 아직 살펴보지 않은 다른 편의점들을
# 모두 iterate하면서 거리가 1000이하라면 que에 등록하고, 해당 편의점이 festival 과의 거리가 1000이하인지
# 확인함으로써 도착지에 도달할 수 있는지 확인한다