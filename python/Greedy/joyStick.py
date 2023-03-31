def solution(name):
    answer = 0
    a_count = 0
    for i in range(len(name)):
        count = ord(name[i])
        answer += min(count - 65, 95 - count + 1)
        if name[i] == 'A':
            a_count += 1

    print(answer)

name = "JAN"
solution(name)