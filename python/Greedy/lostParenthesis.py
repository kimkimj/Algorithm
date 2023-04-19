given = input().split('-')
total = 0
for i in range(len(given)):
    sum = 0
    arr = given[i].split('+')
    for num in arr:
        sum += int(num)
    if i == 0:
        total += sum
    else:
        total -= sum
print(total)