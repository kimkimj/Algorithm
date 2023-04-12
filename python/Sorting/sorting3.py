import sys

arr = [0] * 10001
n = int(input())
for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(1, 10001):
    for j in range(arr[i]):
        print(i)

