def solution(number, k):
    start = 0
    new_number = ''
    while k > 0:
        if start + k >= len(number):
            start = len(number)
            k = 0
        else:
            slice = number[start: start + k + 1]
            max_number = max(slice)
            new_number += max_number

            index_max_number_in_slice = slice.find(max_number)
            k -= index_max_number_in_slice
            start = start + index_max_number_in_slice + 1


    if start < len(number) - 1:
        new_number += number[start:]

    print(new_number)
solution("4321", 1)

