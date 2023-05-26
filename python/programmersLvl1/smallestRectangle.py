def solution(sizes):
    for _ in range(len(sizes)):
        largest_a = sizes[0][0]
        largest_b = sizes[0][1]
        index_a = 0
        index_b = 0

        # find the largest a and b and their indexes
        for i in range(len(sizes)):
            if sizes[i][0] > largest_a:
                largest_a = sizes[i][0]
                index_a = i

            if sizes[i][1] > largest_b:
                largest_b = sizes[i][1]
                index_b = i

        # can a and b swich and result in a smaller area
        if largest_a < largest_b and sizes[i][1] <= largest_a:
            corresponding_b = sizes[i][1]
            sizes[i][1] = largest_a
            sizes[i][0] = corresponding_b

        if largest_b < largest_a and sizes[i][0] <= largest_b:
            corresponding_a = sizes[i][0]
            sizes[i][0] = largest_b
            sizes[i][1] = corresponding_a

    return largest_a * largest_b

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))













