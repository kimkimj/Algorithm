n = int(input())
target = int(input())

start = 1
end = n * n
answer = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(1, n + 1):
        count += min(n, mid // i) #n개가 넘어가면 column의 limit인 n을 초과하는 것이기 때문에

    if count >= target:
        end = mid - 1

    else:
        start = mid + 1

print(start)

#https://st-lab.tistory.com/281