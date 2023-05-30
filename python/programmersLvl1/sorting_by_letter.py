def solution(strings, n):
    new = []
    for i in strings:
        new.append(i[n] + i)
    new.sort()

    answer = []
    for i in new:
        answer.append(i[1:])
    return answer

# sort, sorted에 key인자를 넣어줌으로써 정렬 기준을 정할 수 있다
def solution2(strings, n):
    return sorted(strings, key=lambda x:(x[n], x))