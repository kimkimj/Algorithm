n = int(input())

d = [0] * 3001

# 1은 0
for i in range(2, n + 1):
    # 우선 2, 3, 5 아무것도 나누어지지 않는 경우에는 i의 인덱스를 1 줄여줍니다. (횟수는 +1)
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[n])

