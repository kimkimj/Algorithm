def solution(cards1, cards2, goal):
    index1 = 0
    index2 = 0
    for word in goal:
        #처음에는 cards1[index1:]으로 index부터 배열의 끝까지에서 단어를 찾도록 해서 틀렸다
        # 단어를 skip할 수 없으므로 cards1[index1]이어야 한다
        if index1 < len(cards1) and word == cards1[index1]:
            index1 += 1
        elif index2 < len(cards2) and word == cards2[index2]:
            index2 += 1
        else:
            return 'No'
    return 'Yes'

cards1 =  ["def", "bcd"]
cards2 = ["b", "c", "d"]
goal = ["bcd"]
print(solution(cards1, cards2, goal))