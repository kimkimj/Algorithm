str = input()
for _ in range(int(input())):
    target, a, b = input().split()
    a, b = int(a), int(b)

    count = str[a: b + 1].count(target)
    print(count)