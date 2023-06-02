def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    total = 0
    for b in babbling:
        prev = ""
        end = 1
        for i in range(len(b)):
            word = b[: end]
            if word == prev:
                break
            if word in sounds:
                b = b[end:]
                if len(b) == 0:
                    total += 1
                    break
                prev = word
                end = 0
            end += 1

    print(total)

def solution2(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer

solution(["aya", "yee", "u", "maa"])
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
