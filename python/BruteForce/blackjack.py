n, m = map(int, input().split())
cards = list(map(int, input().split()))
closest = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range (j + 1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m and sum > closest:
                closest = sum
print(closest)

# for k in range(i + 2) 대신 (j + 1)을 사용
        # if k always starts at i + 2, it will eventually stay ahead of j which can
        # start at say j = 5 and k = 3
# sum has to be less than or equal to m
# instead of using absolute value, which accounts for when the sum exceeds m,
#      take the sum as the closest if it is bigger