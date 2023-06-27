def solution(X, Y):
    x = [0] * 10
    for i in range(len(X)):
        x[int(X[i])] += 1

    y = [0] * 10
    for i in range(len(Y)):
        y[int(Y[i])] += 1

    result = ''
    for i in reversed(range(10)):
        result += str(i) * min(x[i], y[i])

    # string의 사이즈가 0인 케이스를 처음으로 체크해야 밑에 result[0]가 index out of bound 에러가 나지 않는다
    if not result:
        return "-1"
    if result[0] == '0':
        return '0'
    return result

x = "100"
y = "2345"
print(solution(x, y))