def solution(s):
    count = 0
    for i in range(len(s)):
        new_str = s[i:] + s[:i]
        stack = []
        for p in new_str:
            if not stack:
                stack.append(p)
            else:
                pair = stack[-1]
                if (pair == '{' and p == '}') or (pair == '(' and p == ')') or (pair == '[' and p == ']'):
                    stack.pop()
                else:
                    stack.append(p)
        if not stack:
            count += 1
    return count

s = "[)(]"
print(solution(s))