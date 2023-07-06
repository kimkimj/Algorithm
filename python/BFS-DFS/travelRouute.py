from collections import defaultdict
def solution(tickets):
    path = []
    graph = defaultdict(list)

    # graph[시작지] - 도착지
    for start, end in tickets:
        graph[start].append(end)

    # 도착점 리스트 역순 정렬
    for airport in graph.keys():
        graph[airport].sort(reverse = True)

    stack = ["ICN"]

    #DFS
    while stack:
        current = stack.pop()
        # current가 시작지인 티켓이 없거나 current를 시작점으로 하는 티켓이 없는 경우
        if current not in graph or not graph[current]:
            path.append(current)
        else:
            stack.append(current)
            stack.append(graph[current].pop())

    # path를 뒤집어서 반환
    return path[::-1]
