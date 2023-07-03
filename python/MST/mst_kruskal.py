import sys

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

def find_parent(x):
    while parent[x] != x:
        x = parent[x]
    return x

def uninon_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        uninon_parent(a, b)
        total_cost += cost

print(total_cost)