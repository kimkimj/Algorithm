def solution(n):
    ones_in_binary = bin(n).count('1')
    while True:
        n += 1
        if ones_in_binary == bin(n).count('1'):
            return n

print(solution(78))


# str(bin(n)[2:]).count('1')
# str로 변환할 필요 없이 bin(n).count('1')
