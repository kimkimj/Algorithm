def solution(brown, yellow):
    answer = []
    for i in range(1, brown):
        height = (brown - 2 * i + 4) / 2
        if height.is_integer():
            height = int(height)
            if i >= height and height * i - brown == yellow:
                return [i, int(height)]
    return []

brown = 10
yellow = 2
print(solution(brown, yellow))
