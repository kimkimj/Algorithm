from itertools import permutations

def solution(k, dungeons):
    current_tiredness = k
    max_dungeon = 0
    for order in permutations(range(0, len(dungeons))):
        count = 0
        while current_tiredness > 0:
            for d in order: # visit dugeon in the order of perm
                if current_tiredness >= dungeons[d][0] and current_tiredness - dungeons[d][1] >= 0:
                    count += 1
                    current_tiredness -= dungeons[d][1]
                else:
                    current_tiredness = -1
        max_dungeon = max(count, max_dungeon)
        current_tiredness = k
    print(max_dungeon)

def solution2(k, dungeons):
    current_tiredness = k
    max_dungeon = 0
    for order in permutations(dungeons):
        count = 0
        while current_tiredness > 0:
            for minimum, consumption in order: # visit dugeon in the order of perm
                if current_tiredness > minimum and current_tiredness - consumption >= 0:
                    count += 1
                    current_tiredness -= consumption
                else:
                    current_tiredness = -1
        max_dungeon = max(count, max_dungeon)
        current_tiredness = k
    print(max_dungeon)


k = 80
dungeons = [[80,20],[50,40],[30,10]]
solution(k, dungeons)