n, m = map(int, input().split())
cards = list(map(int, input().split()))
closest = 0
for i in range(n-2):
    for j in range(i + 1, n - 1):
        for k in range (i + 2, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum > m and abs(m - sum) < abs(m - closest):
                closest = sum
print(closest)