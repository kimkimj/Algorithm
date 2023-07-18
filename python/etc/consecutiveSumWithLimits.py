# 예시를 다시 보니 "모든 연속적인 이틀간의 온도의 합"을 구한다는 것을 알았다
# 나는 모든 연속적인 합이 아니라 합이 예전 합보다 클 때만 합을 구했는데 그게 아니라 "모든 연속적인 합"을 구해야 했다
# 그래서 que를 만들어 que의 size가 K가 아닐때는 무조건 que에 추가하고 합에 더하고
# 사이즈가 k이상이면 que의 맨 앞에 있는 element를 que와 sum에서 제거한 후 새로운 element를 추가해 greatest와 비교한다


from collections import deque

N, K = map(int, input().split())
temp = list(map(int, input().split()))

greatest = sum(temp[0:K])
sum = 0
que = deque([])

for t in temp:
    if len(que) < K:
        sum += t
        que.append(t)
    else: # len(que) >= K:
        sum -= que.popleft()
        sum += t
        que.append(t)

    if len(que) >= K and sum > greatest:
        greatest = sum

print(greatest)

# 7 6
# -100 -100 -100 -100 -100 -100 -100
