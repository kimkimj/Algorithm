
def backtrack(sum, n, visited):
    if sum > n:
        return 0

    if sum == n:
        return 1

    visited[sum] = 1

    return backtrack(sum + 1, n, visited) + backtrack(sum + 2, n, visited)

def solution(n):
    count = 0
    visited = [0] * n
    return backtrack(0, n, visited)

print(solution(3))