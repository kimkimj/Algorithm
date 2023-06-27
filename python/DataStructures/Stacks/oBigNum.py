# 백준 오큰수
import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = [-1] * n
dq = []

for i in range(n):
    while len(dq) > 0 and arr[dq[0][1]] < arr[i]:
        idx = heapq.heappop(dq)[1]
        result[idx] = arr[i]

    heapq.heappush(dq, (arr[i], i))

print(' '.join(map(str, result)))


