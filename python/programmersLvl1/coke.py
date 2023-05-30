def solution(a, b, n):
    total = 0
    while n >= a:
        earned = n // a * b
        n = n % a + earned
        total += earned
    print(total)

solution(3, 1, 20)