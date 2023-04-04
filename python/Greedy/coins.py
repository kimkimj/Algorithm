n, total = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

count = 0
temp_total = total
while temp_total > 0:
    largest_coin = coins[0]
    i = 0
    while temp_total > coins[i]:
        largest_coin = coins[i]
        i += 1
    count += temp_total // largest_coin
    temp_total = temp_total % largest_coin
print(count)