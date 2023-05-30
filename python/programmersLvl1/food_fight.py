def solution(food):
    player1 = ''
    player2 = ''
    for i in range(1, len(food)):
        new_string = str(i) * (food[i] // 2)
        player1 += new_string
        player2 = new_string + player2

    return player1 + '0' + player2

print(solution([1, 7, 1, 2]))
