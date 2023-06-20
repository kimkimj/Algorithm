from collections import deque, defaultdict

def dfs(graph):
    stack = deque()
    stack.append("ICN")
    path = []

    while stack:
        start = stack.pop()
        # 더 이상 해당 도시에서 춟발하는 항공권이 없을 때
        if start not in graph or not graph[start]:
            path.append(start)

        else:
            # 해당 도시를 다시 stack에 넣고 도착지도 stack에 추가
            stack.append(start)
            stack.append(graph[start].pop)

    # path를 reverse해서 반환
    return path[::-1]

def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    for start in graph.keys():
        graph[start].sort(reverse = True)

    return dfs(graph)

# https://gurumee92.tistory.com/165
