import math
def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    deployment = []
    max = days[0]
    count = 0
    for i in range(len(days)):
        if days[i] <= max:
            count += 1
        else:
            deployment.append(count)
            max = days[i]
            count = 1

    deployment.append(count)
    print(deployment)

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])

