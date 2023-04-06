#a, b, c, d, e, f = map(int, input().split())
a, b, c, d, e, f = 1, 3, -1, 4, 1, 7

y = (f - d * c // a) // (e - b * d // a)
x = (c - b * y) // a

print(x, y)