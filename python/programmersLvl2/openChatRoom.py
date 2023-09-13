def solution(record):
    dict = {}
    answer = []
    for r in record:
        line = r.split()
        if len(line) == 2:
            uid = line[1]
            answer.append(uid + ":" + "님이 나갔습니다.")

        else:
            status, uid, name = line[0], line[1], line[2]
            if status == "Enter":
                dict[uid] = name
                answer.append(uid + ":"+ "님이 들어왔습니다.")

            elif status == "Change":
                dict[uid] = name

    for i in range(len(answer)):
        a = answer[i]
        uid, line = a.split(":")
        uid = dict[uid]
        answer[i] = uid + line
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
