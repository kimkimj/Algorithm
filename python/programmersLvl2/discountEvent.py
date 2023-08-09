def solution(want, number, discount):
    wishlist = {}
    days = 0
    for start_day in range(len(discount) - 10 + 1):
        for i in range(len(want)):
            wishlist[want[i]] = number[i]

        can_be_added = True
        for i in range(start_day, start_day + 10):
            if discount[i] not in wishlist or wishlist[discount[i]] - 1 < 0:
                can_be_added = False
                break
            else:
                wishlist[discount[i]] -= 1

        if can_be_added:
            days += 1
    return days

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))


