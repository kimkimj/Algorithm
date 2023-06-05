def solution(keymap, targets):
    dict = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in dict:
                dict[key[i]] = i + 1
            else:
                dict[key[i]] = min(dict[key[i]], i + 1)
    answer = []
    for t in targets:
        total = 0
        for letter in t:
            if letter in dict:
                total += dict[letter]
            else:
                total = -1
                break
        answer.append(total)
    print(answer)

keymap = ["AA"]
targets = ["B"]
solution(keymap, targets)