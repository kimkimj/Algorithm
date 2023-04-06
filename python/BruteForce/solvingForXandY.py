a, b, c, d, e, f = map(int, input().split())
#a, b, c, d, e, f = 1, 3, -1, 4, 1, 7

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            break

# brute force이고 문제에 -999 이상  999 이하의 수만 들어갈 수 있다고 명시되어 있기
# 때문에 range 안의 모든 수를 방정식에 대입하면 풀 수 있다