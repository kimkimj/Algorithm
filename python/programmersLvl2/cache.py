def solution(cacheSize, cities):
    from collections import deque

    if cacheSize == 0:
        return len(cities) * 5
    total = 0
    que = deque()
    for city in cities:
        city = city.lower()
        if city in que:
            total += 1
            que.remove(city)
            que.append(city)

        else:
            total += 5
            if len(que) == cacheSize:
                que.popleft()
            que.append(city)
    return total

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))


