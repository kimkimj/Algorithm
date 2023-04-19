n = int(input())
arr = list(map(int, input().split()))

arr.sort()
sum = 0
total_sum = 0
for i in range(n):
    sum += arr[i]
    total_sum += sum
print(total_sum)