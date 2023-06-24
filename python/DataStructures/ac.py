# https://st-lab.tistory.com/221
# https://clap0107.tistory.com/16
#배열을 뒤집는 과정을 직접 구현하면 시간초과가 난다

from collections import deque

n = int(input())
for _ in range(n):
    actions = input()
    length = int(input())

    if length == 0:
        input() # 이걸 안해주면 length = 0일때 input을 받지 않기 때문에
                # 다음 test case에서 input을 process할 때 밀리게 된다 -> value error
                # 예제에서는 length = 0인 case가 맨 마지막에 나왔기 때문에 문제가 없었던 것
        arr = deque()
    else:
        arr = deque(input()[1:-1].split(','))

    reverse = -1 # negative means not reversed
    error = False

    for a in actions:
        if a == 'R':
            reverse *= -1

        else:
            if not arr:
                error = True
                break

            if reverse == 1:
                arr.pop()
            else:
                arr.popleft()

    if error:
        print("error")
    else:
        if reverse == 1:
            arr.reverse()

        print("[" + ','.join(arr) + "]")

