def solution(dartResult):
    scores = []
    for i in range(len(dartResult)):
        c = dartResult[i]
        if c.isdigit():
            if c == '0' and dartResult[i - 1] == '1':
                scores.pop()
                scores.append(10)
            else:
                scores.append(int(c))
        elif c.isalpha():
            score = scores.pop()
            if c == 'D':
                score *= score
            elif c == 'T':
                score = score * score * score

            scores.append(score)
        else:
            current = scores.pop()

            if c == '*':
                if len(scores) == 0:
                    scores.append(current * 2)
                else:
                    prev = scores.pop()
                    scores.append(prev * 2)
                    scores.append(current * 2)
            else: # c == #
                scores.append(current * - 1)

    return sum(scores)

dartResult = "1D2S0T"
print(solution(dartResult))