import sys

input = sys.stdin.readline

v, e = map(int, input().split())

# parent root를 자기 자신으로
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# 모든 edge와 edge weight 을 저장
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# edge weight을 기준으로 오름차순 정렬
edges.sort()

#def find_root(x):
# while parent[x] != x:
#     x = parent[x]
# return x
def find_root(parent, x):
    if parent[x] != x: # ex)
        parent[x] = find_root(parent, parent[x])
    return parent[x]
def union_roots(a, b):
    root_a = find_root(parent, a)
    root_b = find_root(parent, b)

    if root_a < root_b:
        parent[b] = root_a
    else:
        parent[a] = root_b

total = 0
# iterate through the edges in the order of edge weight
for i in range(e):
    cost, a, b = edges[i]

    # a와 b의 부모가 다르면 union연산 수행해서 mst에 포함
    if find_root(parent, a) != find_root(parent, b):
        union_roots(a, b)
        total += cost

print(total)