n, m = map(int, input().split())
comb = []

def recur():
    if len(comb) == m:
        print(' '.join(map(str, comb)))
        return

    for i in range(1, n + 1):
        if i not in comb:
            comb.append(i)
            recur()
            comb.pop()

recur()

