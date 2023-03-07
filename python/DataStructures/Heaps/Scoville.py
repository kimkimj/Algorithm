from queue import PriorityQueue
def main():
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7
    print(solution(scoville, k))


def solution(scoville, K):
    que = PriorityQueue()
    for i in range(len(scoville)):
        que.put(scoville[i])

    answer = 0
    num = 0
    for i in range(len(scoville) - 1):
        num = que.get()
        if num < K:
            num += que.get() * 2
            answer += 1
            que.put(num)
        else:
            return answer

    return -1

if __name__ == '__main__':
    main()