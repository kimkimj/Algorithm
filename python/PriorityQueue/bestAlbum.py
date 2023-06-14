import heapq

def solution(genres, plays):
    # genre를 key로 하고, 같은 genre가 나오면 plays 수를 더한다
    dict_genre = {}
    for i in range(len(genres)):
        g = genres[i]
        if g not in dict_genre:
            dict_genre[g] = -plays[i]
        else:
            dict_genre[g] = dict_genre[g] - plays[i]

    # priority queue에 장르의 총 play 수와 해당 id의 play수를 priority로 저장한다
    pq = []
    for i in range(len(plays)):
        g = genres[i]
        p = dict_genre[g]
        heapq.heappush(pq, (p, -plays[i], i))

    # limits 에 genre를 key로, 2번 이상 pq에서 제거가 되었는지를 value로 저장한다
    # 2번 이하로 저장되었으면 answer에 저장한다
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



