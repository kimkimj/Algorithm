n, total = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

count = 0
for i in reversed(range(n)):
    count += total // coins[i]
    total = total % coins[i]

print(count)