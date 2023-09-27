n, m = map(int, input().split())
comb = []

def recur():
    if len(comb) == m:
        print(*comb)
        return

    for i in range(1, n + 1):
        if len(comb) == 0 or i >= comb[-1]:
            comb.append(i)
            recur()
            comb.pop()

recur()