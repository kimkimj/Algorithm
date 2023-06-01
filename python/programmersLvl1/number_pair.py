def solution(X, Y):
    x = [0] * 10
    for digit in X:
        x[int(digit)] += 1

    y = [0] * 10
    for digit in Y:
        y[int(digit)] += 1

    answer = ""
    for i in reversed(range(10)):
        answer += str(i) * min(x[i], y[i])
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer

print(solution("100", "203045"))
