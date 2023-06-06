def solution(s, skip, index):
    letter = []
    dict = {}
    for i in range(26):
        next_alphabet = chr(ord('a') + i)
        if next_alphabet not in skip:
            letter.append(next_alphabet)
            dict[next_alphabet] = len(letter) - 1
    answer = ''
    for char in s:
        new_idx = dict[char] + index

        # consider the case in which 'index' is greater than the length of letter[]
        # eg. idx = 4 where len(letter) = 5 and index = 20
        # new_idx = 20 - 5 = 15 and letter[15] -> runtime error
        while new_idx >= len(letter):
            new_idx -= len(letter)
        answer += letter[new_idx]
    print(answer)

s = "aukks"
skip = "wbqd"
index = 5
solution(s, skip, index)

# https://school.programmers.co.kr/learn/courses/30/lessons/155652

