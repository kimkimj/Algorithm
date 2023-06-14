import heapq

def solution(genres, plays):
    dict_genre = {}
    for i in range(len(genres)):
        g = genres[i]
        if g not in dict_genre:
            dict_genre[g] = -plays[i]
        else:
            dict_genre[g] = dict_genre[g] - plays[i]

    pq = []

    for i in range(len(plays)):
        g = genres[i]
        p = dict_genre[g]
        heapq.heappush(pq, (p, -plays[i], i))

    answer = []
    limits = {}
    for i in range(len(pq)):
        index = heapq.heappop(pq)[2]
        g = genres[index]

        if g not in limits:
            limits[g] = 1
        elif limits[g] == 1 or limits[g] == 2:
            limits[g] = limits[g] + 1

        if limits[g] <= 2:
            answer.append(index)

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))



