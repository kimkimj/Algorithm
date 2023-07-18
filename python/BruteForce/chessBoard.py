N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

total = float("INF")
prev_1 = "W"
prev_2 = "B"
result = []
for i in range(0, N - 7):
    for j in range(0, M - 7):
        current = board[i][j]
        count_1, count_2 = 0 ,0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # 더한 숫자가 even 일 때 count_1은 검은색 이어야 하고, count_2는 흰색이 여야한다
                if (a + b) % 2 == 0:
                    if board[a][b] != "B":
                        count_1 += 1
                    else:
                        count_2 += 1
                else:
                    # board should be white for count1 and black for count 2
                    if board[a][b] != "W":
                        count_1 += 1
                    else:
                        count_2 += 1
        result.append(count_1)
        result.append(count_2)
print(min(result))











