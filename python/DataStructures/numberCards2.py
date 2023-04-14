n = int(input())
owned = list(map(int, input().split()))
dict = {}
for i in range(n):
    num = owned[i]
    if num in dict:
        dict[num] = dict[num] + 1
    else:
        dict[num] = 1

m = int(input())
given = list(map(int, input().split()))

for i in range(m):
    if given[i] in dict:
        print(dict[given[i]], end = " ")
    else:
        print(0, end = " ")


