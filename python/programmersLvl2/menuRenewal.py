from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    menus = set()
    for o in orders:
        for single in o:
            menus.add(single)
    # put every single menu in the set

    answer = []
    for num_menu in course:
        customers = defaultdict(list)
        largest = 0
        for c in combinations(menus, num_menu):
            combo = ''.join(list(c))
            count = 0
            for o in orders:
                letters = 0
                for c in o:
                    if c in combo:
                        letters += 1
                if letters == len(combo):
                    count += 1

            if count > largest:
                largest = count

            if count >= 2:
                customers[count].append(combo)

        for c in customers:
            print(c)
            if c == largest:
                for combo in customers[c]:
                    answer.append(''.join(sorted(combo)))
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))