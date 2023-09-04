# https://kimmeh1.tistory.com/485
# 0 ~ (순서 * 인원수) 만큼의 수를 n 진법으로 구한다
    # 10진법을 n 진법으로 구하는 방법은 쉽다. 숫자를 n으로 나눈 몫이 0이 될때까지 구하고 (truncate)
    # 나머지를 reverse order로 합치면 된다
# n 진법으로 바뀐 숫자들을 모두 합하고, 인덱스를 p - 1 부터 m씩 늘려간다

def convert_base(num, base):
    temp = "0123456789ABCDEF"

    if num == 0:
        return "0"

    result = ""
    while num > 0:
        number = temp[num % base]
        result += str(number)
        num //= base
    return ''.join(reversed(result))

def solution(n, t, m, p):
    numbers = ""
    for i in range(m * t): # 왜 m * t인지는 잘 모르겠다
        numbers += convert_base(i, n)

    answer = ""
    for i in range(p - 1, t * m, m): #len(numbers)로 하면 작동안함
        answer += numbers[i]

    return answer

print(solution(2, 4, 2, 1))