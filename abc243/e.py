from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd
# from itertools import permutations, combinations, product
class UnionFind:
    def __init__(self, N):
        # N = data size
        self.n = N
        self.parents = [-1] * N

    def find(self, x):
        # find x's root
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # unite x and y
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False
        if -(self.parents[rx]) < -(self.parents[ry]):
            rx, ry = ry, rx
        self.parents[rx] += self.parents[ry]
        self.parents[ry] = rx
        return True

    def size(self, x):
        # size of group of x's root
        return -(self.parents[self.find(x)])

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


N, M = map(int, input().split())
E = []
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    E.append([a, b, c])
E.sort(key=lambda x: x[2])

D = [[INF] * N for _ in range(N)]
for i in range(N):
    D[i][i] = 0
U = UnionFind(N)


def Update():
    global D
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], (D[i][k] + D[k][j]))


cnt = 0
for a, b, c in E:
    if U.same(a, b):
        if c < D[a][b]:
            D[a][b] = c
            D[b][a] = c
            Update()
        else:
            cnt += 1
    else:
        U.union(a, b)
        D[a][b] = c
        D[b][a] = c
        Update()

print(cnt)
