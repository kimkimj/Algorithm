def solution(players, callings):
    dict = {}
    for i in range(len(players)):
        a = players[i]
        dict[players[i]] = i

    for name in callings:
        current_rank = dict[name]
        prev_player = players[current_rank - 1]

        players[current_rank] = prev_player
        players[current_rank - 1] = name

        dict[prev_player] = current_rank
        dict[name] = current_rank - 1

    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))
