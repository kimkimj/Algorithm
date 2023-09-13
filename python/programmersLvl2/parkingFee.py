from collections import defaultdict
import math

def solution(fees, records):
    # 요금 저장
    first_min = fees[0]
    first_min_fee = fees[1]
    min_to_charge = fees[2]
    fee_per_min = fees[3]

    answer = {}
    license_plates = set()
    dict = defaultdict(list)

    for r in records:
        time, plate, cat = r.split()
        dict[plate].append(time)
        license_plates.add(plate)

    for car in dict:
        total_min = 0
        hour_in = 0
        time_list = dict[car]
        for i in range(len(time_list)):
            hour, minute = map(int, time_list[i].split(":"))
            if i % 2 == 0: #입차
                total_min += 60 - minute
                hour_in = hour + 1
            else: #출차
                total_min += minute
                total_min += (hour - hour_in) * 60

        if len(time_list) % 2 == 1: #odd
            total_min += (23 - hour_in) * 60 + 59

        # 요금 계산
        if total_min <= first_min:
            answer[car] = first_min_fee
        else:
            answer[car] = first_min_fee + math.ceil((total_min - first_min) / min_to_charge) * fee_per_min

    result = []
    #return answer in the order of the license plate
    license_plates = sorted(license_plates)
    for num in license_plates:
        result.append(answer[num])

    return result


fees = [1, 461, 1, 10]
records =["00:00 1234 IN"]
print(solution(fees, records))