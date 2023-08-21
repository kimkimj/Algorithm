def solution(s):
    s= s.strip("{}")
    s = s.split("},{")

    sets = [0] * len(s)
    for group in s:
        a = set((group.split(",")))
        sets[len(a) - 1] = a

    answer = []
    for i in range(len(sets)):
        for e in sets[i]:
            e = int(e)
            if e not in answer:
                answer.append(e)

    return answer

s = "{{20,111},{111}}"
solution(s)




