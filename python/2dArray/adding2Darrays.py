n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)

for r in range(n):
    for c in range(m):
        print(a[r][c] + b[r][c], end = ' ')
    print()