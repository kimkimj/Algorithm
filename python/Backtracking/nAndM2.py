n, m = map(int, input().split())
comb = []

def recur():
    if len(comb) == m:
        print(*comb)
        return

    for i in range(1, n + 1):
        if len(comb) == 0 or (i not in comb and comb[-1] < i):
            comb.append(i)
            recur()
            comb.pop()

recur()