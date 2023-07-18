from collections import deque

N, K = map(int, input().split())
temp = list(map(int, input().split()))

greatest = sum(temp[0:K])
sum = 0
que = deque([])

for t in temp:
    if len(que) >= K:
        sum -= que.popleft()
    if sum + t >= t or len(que) < K:
        sum += t
        que.append(t)
    else:
        sum = t
        que = deque([t])

    if sum > greatest:
        greatest = sum
print(greatest)

# 7 6
# -100 -100 -100 -100 -100 -100 -100
# https://www.acmicpc.net/problem/2559