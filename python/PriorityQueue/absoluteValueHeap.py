import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))

# to specify the priority of values: heapq.heappush(heap_name, (priority, value))
# to get the value: heapq.heappop(heap_name)[1]