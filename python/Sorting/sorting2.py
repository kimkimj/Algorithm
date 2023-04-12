import sys

n = int(input())
arr = []
for i in range(n):
    # input() 이 sys.stdin.readline() 보다 느리기 때문에
    # sys.stdin.readLine()을 사용해서 시간 초과 문제를 해결
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in range(n):
    print(arr[i])