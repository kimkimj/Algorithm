def solution(name):
    answer = 0
    a_count = 0

    for i in range(len(name)):
        count = ord(name[i])
        k = min(count - 65, 90 - count + 1)
        answer += k
        if name[i] == 'A':
            a_count += 1


    next_a_index = name.find('A')
    if next_a_index != -1:
        while name[next_a_index] == 'A':
            a_count += 1
            next_a_index += 1
    if a_count == 1 and name.find('A') == 0:
        a_count = 0
    answer += len(name) -1 - a_count

    print(answer)

name = "JAN"
solution(name)