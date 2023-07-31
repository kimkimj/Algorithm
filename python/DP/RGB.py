n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        if j == 0:
            cost[i][j] += min(cost[i- 1][1], cost[i- 1][2])

        if j == 1:
            cost[i][j] += min(cost[i - 1][0], cost[i - 1][2])

        if j == 2:
            cost[i][j] += min(cost[i - 1][0], cost[i - 1][1])

print(min(cost[n - 1]))

