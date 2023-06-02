def solution(s):
    base = s[0]
    same, diff = 0, 0
    total = 0

    for i in range(len(s)):
        if s[i] == base:
            same += 1
        else:
            diff += 1
        if same == diff:
            total += 1
            same, diff = 0, 0
            if i +1 < len(s):
                base = s[i + 1]
    if same != diff:
        total += 1
    print(total)

solution("aaabbaccccabba")


