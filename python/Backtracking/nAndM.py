n, m = map(int, input().split())
comb = []

def dfs():
    if len(comb) == m:
        print(*comb)

    for i in range(1, n+ 1):
        if i not in comb:
            comb.append(i)
            dfs()
            comb.pop()


dfs()