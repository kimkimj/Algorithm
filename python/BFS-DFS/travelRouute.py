def solution(tickets):
    dict = {}
    for start, end in tickets:
        if start in dict:
            temp = dict[start]
            temp.append(end)
            temp.sort(reverse=True)
            dict[start] = temp
        else:
            dict[start] = [end]

    que = ["ICN"]
    answer = []
    while que:
        current = que.pop() #pop(0) vs pop()
        answer.append(current)

        if current in dict and dict[current]:
            for neighbor in dict[current]:
                que.append(neighbor)
            dict[current] = []
    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))

