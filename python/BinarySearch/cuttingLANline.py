import sys

input = sys.stdin.readline

k, n = map(int, input().split())
cables = []
for _ in range(k):
    cables.append(int(input()))

# 결과값이 자연수라고 명시했다. 자연수는 1 이상의 모든 정수이다
# 1로 하지 않으면 division by zero가 나오는 케이스가 있다
start = 1
end = max(cables)
result = 0
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        break

    total = 0
    for line in cables:
        total += line // mid

    if total < n:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)


