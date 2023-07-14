import sys
input = sys.stdin.readline

num_house, num_router = map(int, input().split())
houses = [0] * num_house
for i in range(num_house):
    houses[i] = int(input())

houses.sort()

start = houses[0]
end = houses[-1]
answer = 0

while start <= end:
    count = 1
    mid = (start + end) // 2
    current = houses[0]

    for h in houses:
        if h >= current + mid:
            count += 1
            current = h

    if count == num_router:
        print(mid)
        break

    elif count < num_router:
        end = mid - 1

    else:
        start = mid + 1

