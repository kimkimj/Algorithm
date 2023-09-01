from itertools import product
def solution(word):
    answer = 0
    dic = ['A', 'E', 'I', 'O', 'U']
    combos = []

    for i in range(1, 6):
        for c in product(dic, repeat = i):
            combos.append(''.join(list(c)))
        combos.sort()
        return combos.index(word) + 1

# more efficient code: https://alreadyusedadress.tistory.com/297