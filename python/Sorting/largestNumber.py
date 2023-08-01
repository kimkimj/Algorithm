# https://liveloper-jay.tistory.com/138
def solution(numbers):
    dict = {}
    arr = []
    for n in numbers:
        new_num = str(n) * 3
        arr.append(new_num)
        dict[new_num] = n

    arr.sort(reverse=True)
    answer = ''
    for n in arr:
        answer += str(dict[n])

    # 만약 numbers=[0,0,0,0] 이라면 0 이 나와야 한다.
    # join한 값을 int로 만들어 준 후 원하는 return값이 str이기 때문에 다시 str로 변환한다.
    return str(int(answer))

numbers = [0, 0, 0, 0]
print(solution(numbers))
