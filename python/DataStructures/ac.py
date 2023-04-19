n = int(input())

answer = []
for i in range(n):
    actions = list(input())
    length = int(input())
    if length > 0:
        arr = list(map(int, input()[1:-1].split(',')))
    else:
        input()
        arr = ''

    i = 0
    while i < len(actions):
        action = actions[i]
        if action == 'R':
            if i + 1 < len(actions) and actions[i + 1] == 'R':
                i += 1
            else:
                arr.reverse()
        else:
            if len(arr) == 0:
                arr = "error"
                break
            arr.pop(0)
        i += 1
    answer.append(arr)

for i in range(len(answer)):
    print(answer[i])