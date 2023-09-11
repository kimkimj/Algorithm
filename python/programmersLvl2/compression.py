def solution(msg):
    answer = []
    last_index = 26
    dict= {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
    index = 0
    while index < len(msg):
        temp = 0
        length = 1
        while index + length <= len(msg) and msg[index: index + length] in dict:
            word = msg[index: index + length]
            temp = dict[msg[index: index + length]]
            length += 1
        last_index += 1
        dict[msg[index: index + length]] = last_index
        answer.append(temp)
        index += length - 1

    return answer

print(solution("KAKAO"))