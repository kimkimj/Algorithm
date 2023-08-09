from collections import Counter

def solution(want, number, discount):
    wishlist = {}
    for i in range(len(want)):
        wishlist[want[i]] = number[i]

    days = 0
    for start_day in range(len(discount) - 10 + 1):
        if wishlist == Counter(discount[start_day: start_day + 10]):
            days += 1

    return days

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))


