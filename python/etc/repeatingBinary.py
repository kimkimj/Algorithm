def solution(s):
    deleted_zero = 0
    conversion = 0
    length = len(s)
    while s != '1':
        s = s.replace('0', '')
        num = len(s)
        deleted_zero += length - num
        s = '' + bin(num)[2:]
        length = len(s)
        conversion += 1

    return [conversion, deleted_zero]

s = "110010101001"
print(solution(s))