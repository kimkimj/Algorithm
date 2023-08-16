def one_letter_diff(current, comparison):
    diff_count = 0
    for k in range(len(current)):
        if current[k] != comparison[k]:
            diff_count += 1
    if diff_count == 1:
        return True
    return False

def solution(begin, target, words):
    graph = {}
    graph[begin] = []
    for word in words:
        graph[word] = []
        if one_letter_diff(begin, word):
            graph[begin].append(word)

    for i in range(len(words)):
        current = words[i]
        for j in range(i + 1, len(words)):
            comparison = words[j]

            if one_letter_diff(current, comparison):
                graph[current].append(comparison)
                graph[comparison].append(current)

    answer = float("INF")
    stack = [(begin, set(), 0)]
    while stack:
        current, visited, count = stack.pop()
        visited.add(current)
        if current == target:
            answer = min(answer, count)
            break

        for changeable in graph[current]:
            if changeable not in visited:
                stack.append((changeable, visited, count + 1))

    if answer == float("INF"):
        print(0)
    else:
        print(answer)

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
solution(begin, target, words)
