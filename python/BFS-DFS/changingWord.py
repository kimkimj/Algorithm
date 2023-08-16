from collections import deque

def solution(begin, target, words):

    que = deque([(begin, 0)])
    visited = set()
    while que:
        current_word, count = que.popleft()

        if current_word == target:
            return count

        for word in words:
            letter_diff_count = 0
            for i in range(len(word)):
                if word[i] != current_word[i]:
                    letter_diff_count += 1
            if letter_diff_count == 1:
                if word not in visited:
                    que.append((word, count + 1))
                    visited.add(word)
    return 0



begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))
