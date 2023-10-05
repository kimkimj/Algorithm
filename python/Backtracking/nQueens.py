def dfs(queen, add, subtract, columns, num_queen):
    if num_queen == n - 1:
        return 1

    queen_r, queen_c = queen

    add[queen_r + queen_c] = False
    substract[queen_r - queen_c + n - 1] = False
    columns[queen_c] = False
    rows[queen_r] = False

    count = 0
    for c in range(n):
        if columns[c]:
            for r in range(n):
                if rows[r]:
                    if add[r + c] and substract[r - c + n - 1]:
                        next_queen = (r, c)
                        num_queen += 1
                        count += dfs(next_queen, add, subtract, columns, num_queen)
    return count


n = int(input())
stack = []
count = 0
# for i in range(n):
#     queen = (0, i)
queen = (1, 0)
# initialize cells representing diagonal and straight line
add = [True] * (n * 2 - 1)
substract = [True] * (n * 2 - 1)
columns = [True] * n
rows = [True] * n


count += dfs(queen, add, substract, columns, 1)
print(count)
