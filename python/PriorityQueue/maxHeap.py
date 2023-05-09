import heapq
import sys

input = sys.stdin.readline

heap = []
n = int(input())

count = 0
for _ in range(n):
    num = int(input())

    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, - num)

# heapq.heappop(heap_name)
# heapq.heappush(heap_name, value)