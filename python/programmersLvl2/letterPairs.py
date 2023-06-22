def solution(s):
    # 문자가 홀수 개수면 무조건 남는다
    if len(s) % 2 == 1:
        return 0

    stack = [s[0]]
    for letter in s[1:]:
        if len(stack) > 0 and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)

    if len(stack) == 0:
        return 1
    else:
        return 0



s = "baabaa"
print(solution(s))
