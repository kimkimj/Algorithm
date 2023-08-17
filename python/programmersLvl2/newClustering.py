def toSet(str):
    set1 = []
    for i in range(len(str) - 1):
        sub = str[i: i + 2]
        if sub.isalpha():
            set1.append(sub)
    return set1

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    set1 = toSet(str1)
    set2 = toSet(str2)

    total = len(set1) + len(set2)
    copy_set1 = set1.copy()
    common_count = 0
    for pair in copy_set1:
        if pair in set2:
            set1.remove(pair)
            set2.remove(pair)
            common_count += 1

    total -= common_count
    if total == 0:
        return 	65536
    return int(common_count / total *  65536)

str1 = "E=M*C^2"
str2 = "e=m*c^2"
print(solution(str1, str2))





