def solution(price, money, count):
    sum = 0
    for i in range(1, count + 1):
        sum += price * i

    amount = money - sum
    if amount < 0:
        return abs(amount)
    else:
        return 0


print(solution(3, 31, 4))