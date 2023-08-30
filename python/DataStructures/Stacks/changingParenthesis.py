def solution(p):
    stack = [' ']
    result = ''

    for char in p:
        prev = stack[-1]

        if char == '(':
            if prev == ')':
                result += ')'
                stack.pop()
            else:
                result += '('
                stack.append(char)


        else: # )
            if prev == '(':
                result += ")"
                stack.pop()
            else:
                result += '('
                stack.append(char)

    return result
p = "(())"
print(solution(p))


