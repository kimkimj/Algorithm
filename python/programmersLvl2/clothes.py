from itertools import combinations
def solution(clothes):
    dict = {}
    for clothing, type in clothes:
        if type in dict:
            dict[type] += 1
        else:
            dict[type] = 1

    answer = 1
    for count in dict.values():
        answer *= (count + 1)
    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))