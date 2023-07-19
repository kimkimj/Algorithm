n, m = map(int, input().split())
bills = [int(input()) for _ in range(n)]
d = [float("INF")] * (m + 1)

for i in range(1, m + 1):
    for b in bills:
        if i % b == 0:
            d[i] = min(d[i], i // b)
        else:
            if i - b > 0:
                d[i] = min(d[i], d[i - b] + 1)

if d[m] == float("INF"):
    print(-1)
else:
    print(d[m])