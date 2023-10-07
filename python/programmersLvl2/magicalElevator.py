import math
def solution(storey):
    total = 0
    storey *= 10
    while storey > 0:
        storey *= 0.1
        up = math.ceil(storey * 0.1 ) * 10
        down = math.floor(storey * 0.1) * 10
        if (up - storey) < (storey - down):
            total += (up - storey)
            storey = up
        else:
            total += (storey - down)
            storey = down

    return total

