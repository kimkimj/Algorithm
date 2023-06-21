def solution(n, words):
    # set_words = set(words[0]) 하니 words[0]의 every signle letter 이 set에 따로 들어갔다 (t, a, n, k)
    # set_words = set()
    # set_words = set_words.add(words[0]) 하니까 에러가 났음
    set_words = [words[0]]
    set_words = set(set_words)

    for i in range(1, len(words)):

        if words[i] not in set_words and words[i][0] == words[i - 1][-1]:
            set_words.add(words[i])
        else:
            return [i % n + 1, i // n + 1]

    return [0 , 0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))


