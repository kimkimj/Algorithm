# https://st-lab.tistory.com/221
# https://clap0107.tistory.com/16
#배열을 뒤집는 과정을 직접 구현하면 시간초과가 난다

from collections import deque

n = int(input())

answer = []
for i in range(n):
    actions = list(input().replace('RR', ''))
    length = int(input())
    arr = []
    if length > 2:
        arr = deque(list(input()[1:-1].split(',')))
    else:
        input()
    reverse = False
    for action in actions:
        if len(arr) == 0:
            arr = "error"
            break
        if action == 'R':
            reverse = not reverse
        else:
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if arr == "error":
        print("error")
    else:
        if reverse:
            arr.reverse()
        print('[' + ','.join(arr) + ']')