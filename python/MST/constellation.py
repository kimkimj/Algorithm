import sys
import math
from itertools import combinations

input = sys.stdin.readline
n = int(input())

def kruskal():
    points = []
    parents = {}

    for _ in range(n):
        x, y = map(float, input().split())

        # set the parent of points to themselves
        parents[(x, y)] = (x, y)
        points.append((x, y))

    edges = []
    for c in combinations(points, 2):
        a, b = c
        cost = math.dist(a, b)
        edges.append((cost, a, b))
    edges.sort()

    def find_root(x):
        while x != parents[x]:
            x = parents[x]
        return x

    def union_roots(a, b):
        root_a = find_root(a)
        root_b = find_root(b)

        if root_a < root_b:
            parents[b] = root_a
        else:
            parents[a] = root_b

    mst_cost = 0
    for cost, a, b in edges:
        if find_root(a) != find_root(b):
            union_roots(a, b)
            mst_cost += cost
    print("%.2f" % mst_cost)

kruskal()

