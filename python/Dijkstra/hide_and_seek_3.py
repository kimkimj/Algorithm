import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

subin, dongsang = map(int, input().split())
def dijkstra():
    # edge case: 5 5
    # the code did not check whether or not the location has already been visited
    # and returned the time at which the target code has been visited again
    if subin == dongsang:
        return 0
    queue = []
    heapq.heappush(queue, (0, subin))
    min_dist = [INF] * 100001
    min_dist[subin] = 0
    while queue:
        current_time, current = heapq.heappop(queue)

        # the for loop iterates sequentially
        # current * 2 must be visited first, otherwise if the target location can also be met by
        # current + 1, or current -1, the code will immediately return it with time + 1
        # edge case: 1 2 must return 0, but returns 1
        for time, loc in [(0, current * 2), (1, current + 1), (1, current - 1)]:
            new_time = current_time + time
            if loc == dongsang:
                return new_time

            if 0 <= loc < len(min_dist) and min_dist[loc] > new_time:
                min_dist[loc] = new_time
                heapq.heappush(queue, (new_time, loc))

print(dijkstra())
