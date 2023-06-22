n, m = map(int, input().split())
comb = []
def recur():
    if len(comb) == m:
        print(' '.join(map(str, comb)))
        comb.pop() #왜 여기에 이걸 쓰면 이미 print한게 반복되고 i도 끝가지 가지 않을까?
        return

    for i in range(1, n + 1):
        if i not in comb:
            comb.append(i)
            recur()
            #comb.pop()
recur()

# comb.pop()을 하면 comb 전체가 없어지는 게 아니가 comb[-1]이 사라지는 것이기 때문이다
# 그리고 len(comb)이 m일 때만 pop을 하게 되지만, 사실