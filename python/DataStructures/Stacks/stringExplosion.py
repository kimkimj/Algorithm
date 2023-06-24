str = input()
explosion = input()
stack = []

for i in range(len(str)):
    stack.append(str[i])
    if stack[-1] == explosion[-1]:
        length = len(explosion)

        #while ''.join(stack[-length:]) == explosion: #while loop로 안해도 된다
        if ''.join(stack[-length:]) == explosion:
            for _ in range(length):
                stack.pop()
if not stack:
    print("FRULA")
else:
    print(''.join(stack))
