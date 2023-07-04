import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

stack = []
#ans = []
idx = 0
order = []
for i in range(1, n + 1):
    stack.append(i)
    order.append("+")
    if i == arr[idx]:
        while stack and arr[idx] == stack[-1]:
            #ans.append(stack.pop())
            stack.pop()
            idx += 1
            order.append("-")

if stack:
    print("NO")
else:
    print(*order, sep='\n')