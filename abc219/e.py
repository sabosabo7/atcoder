from sys import exit, flags, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left


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


H = []
for i in range(4):
    A = list(map(int, input().split()))
    for j in range(4):
        if A[j] == 1:
            H.append(6 * (i + 1) + (j + 1))

cnt = 0
for i in range(2 ** 16):
    G = [0] * 36
    # _G = [[0] * 6 for _ in range(6)]
    for j in range(16):
        if (i >> j) & 1:
            x = j // 4
            y = j % 4
            x += 1
            y += 1
            G[x * 6 + y] = 1
            # _G[x][y] = 1

    flag = True
    for h in H:
        flag &= G[h]
    if not flag:
        continue

    UF = UnionFind(36)
    for j in range(36):
        if j // 6 >= 1:
            if G[j] == G[j - 6]:
                UF.union(j, j - 6)

        if j % 6 != 0:
            if G[j] == G[j - 1]:
                UF.union(j, j - 1)

    if len(UF.all_group_members().keys()) == 2:
        cnt += flag

print(cnt)
