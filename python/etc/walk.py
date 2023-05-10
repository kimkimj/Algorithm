def solution(park, routes):
    current_r, current_c = 0, 0
    for i in range(len(park)):
        index = park[i].find('S')
        if index > -1:
            current_r, current_c = i, index

    for r in routes:
        direction, move = r.split(' ')
        dr, dc = 0, 0
        if direction == 'S':
            dr = int(move)
        elif direction == 'N':
            dr = -int(move)
        elif direction == 'E':
            dc = int(move)
        else: # W
            dc = -int(move)

        nr = current_r + dr
        nc = current_c + dc

        if 0 <= nr < len(park) and 0 <= nc < len(park[0]) \
                and park[nr][nc] == 'O':
            if dr != 0:
                for j in range(dr):
                    if park[current_r + j][current_c] == 'X':
                        dr = 0
                        break
                current_r += dr

            else: # dc != 0
                horizontal_path = park[current_r][current_c: nc + 1]
                if horizontal_path.find('X') == -1:
                    current_c = nc
    return [current_r, current_c]

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))