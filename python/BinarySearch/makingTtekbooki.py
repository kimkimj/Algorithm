import sys
input = sys.stdin.readline

n, min_height = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for t in heights:
        if t - mid > 0:
            total += t - mid

    # 절단기의 높이를 늘리면 더 적은 양의 떡이 남고, 낮추면 더 많이 남는다
    # 자른 떡의 양이 min_height이 되지 않는다면 절단기의 높이를 낮춰야 한다 (decrease mid)
    if total < min_height:
        end = mid - 1
    else: # 자른 떡의 양이 min_height과 같거나 그보다 클 때는 절단기의 높이를 늘려야 한다(increase mid)
        result = mid
        start = mid + 1



print(total)
