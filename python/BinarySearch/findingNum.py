
n = 5
given = [4, 1, 5, 2, 3]
#n = int(input())
#given = list(map(int, input().split()))
m = 5
b = [1, 3, 7, 9, 5]

given.sort()
for num in b:
    mid = len(given) // 2
    found = False
    while mid >= 0 and mid < len(given):
        if num == given[mid]:
            found = True
            break
        elif num < given[mid]:
            mid //= 2
        else:
            mid = (len(given) + mid) // 2
    if found == False:
        print(0)
    else:
        print(1)

