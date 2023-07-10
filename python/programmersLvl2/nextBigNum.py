def solution(n):
    ones_in_binary = bin(n).count('1')
    while True:
        n += 1
        if ones_in_binary == bin(n).count('1'):
            return n

# str(bin(n)[2:]).count('1')

# str로 변환할 필요 없이 bin(n).count('1')
def solution2(n):
    num_one = bin(n).count('1')

    while True:
        n += 1
        if bin(n).count('1') == num_one:
            return n

print(solution2(78))















