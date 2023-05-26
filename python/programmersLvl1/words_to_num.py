def solution(s):
    dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
            'five':5, 'six':6, 'seven':7,'eight':8, 'nine':9}

    num = ""
    word = ""
    for i in range(len(s)):
        if 'a' <= s[i] <'z':
            word += s[i]
            if word in dict:
                num += str(dict[word])
                word = ""
        else:
            num += str(s[i])
    return int(num)

print(solution("oneoneone"))

