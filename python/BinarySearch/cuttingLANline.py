import sys
input = sys.stdin.readline

n, req = map(int, input().split())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

# 결과값이 자연수라고 명시했다. 자연수는 1 이상의 모든 정수이다
start = 1
end = max(arr)
result = 1

while start <= end:
    total = 0
    mid = (start + end) // 2

    for line in arr:
        total += line // mid

    if total >= req:
        start = mid + 1
        result = mid

    else:
        end = mid -1

print(result)