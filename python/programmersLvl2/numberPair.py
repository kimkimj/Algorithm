from collections import Counter

def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)

    result = ''
    for i in reversed(range(0, 10)):
        result += str(i) * min(x[str(i)], y[str(i)])

    if len(result) == 0:
        return "-1"

    if result[0] == "0":
        return "0"

    return result

solution("100", "203045")
