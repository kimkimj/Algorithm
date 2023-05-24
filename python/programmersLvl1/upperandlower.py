def solution(s):
    str = ''
    words = s.split(' ')
    for i in range(len(words)):
        for j in range(len(words[i])):
            if j == 0 or j % 2 == 0:
                str += words[i][j].upper()
            else:
                str += words[i][j].lower()
        str += ' '
    return str[:-1]

print(solution("a a you"))