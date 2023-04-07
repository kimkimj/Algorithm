n = 20
count = 0
for i in range(666, 10001):
    if str(i).find('666') != -1:
        count += 1
        if count == n:
            print(i)
            break