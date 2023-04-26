
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

graphs = [[0] * n] * n
counts = [0]

for i in range(n):
    for j in range(n):
        graph_num = 0
        current = arr[i][j]
        if current == 1:
            if (i - 1 >= 0 and arr[i - 1][j] == 1):
                # 윗칸과 연결 (exisitng node)
                graph_num = graphs[i - 1][j]
                counts[graph_num] += 1

            elif j - 1 >= 0 and arr[i][j - 1] == 1:
                #왼쪽 칸과 연결 (existing node)
                graph_num = graphs[i][j + 1]
                counts[graph_num] += 1

            elif j - 1 >= 0 and arr[i][j - 1] == 1:
                # 위에 동과 연결되어 있다 (existing node)
                graph_num = graphs[i][j - 1]
                counts[graph_num] += 1

            elif (i + 1 < len(arr) and arr[i + 1][j] == 1) \
                    or (j + 1 < len(arr[i]) and arr[i][j + 1] == 1):
                # 오른쪽이나 아랫칸과 연결되어 있음 (unexplored)
                # 새로운 동
                graph_num = len(counts)
                counts.append(1)
            else:
                # isolated
                graph_num = len(counts)
                counts.append(1)

            graphs[current] = graph_num

print(len(counts) - 1)
print(*sorted(counts))