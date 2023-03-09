import heapq
def main():
    scoville = [1, 2, 3]
    k = 11
    print(solution(scoville, k))


def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0

    while len(scoville) != 1:
        num = heapq.heappop(scoville)
        if num < K:
            num += heapq.heappop(scoville) * 2
            answer += 1
            heapq.heappush(scoville, num)
        else:
            return answer

    # 이 코드를 더하기 전까지는 heapq의 마지막 요소는 검사하지 않았기 때문에 마지막 요소로서 모든 요소가 k이상이 되어도 -1을 반환했다
    if scoville[0] < K:
        return -1
    return answer

if __name__ == '__main__':
    main()