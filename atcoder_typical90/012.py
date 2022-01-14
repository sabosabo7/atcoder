from sys import exit, flags, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

H, W = map(int, input().split())
Q = int(input())


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


G = [[0] * W for _ in range(H)]
D = UnionFind(W * H)
flag = False
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c = q[1:]
        r -= 1
        c -= 1
        G[r][c] = 1
        if c - 1 >= 0 and G[r][c - 1] == 1:
            D.union(r * W + c, r * W + c - 1)
        if r - 1 >= 0 and G[r - 1][c] == 1:
            D.union(r * W + c, (r - 1) * W + c)
        if c + 1 <= W - 1 and G[r][c + 1] == 1:
            D.union(r * W + c, r * W + c + 1)
        if r + 1 <= H - 1 and G[r + 1][c] == 1:
            D.union(r * W + c, (r + 1) * W + c)
    else:
        r1, c1, r2, c2 = q[1:]
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1

        if G[r1][c1] == 1 and G[r2][c2] == 1 and D.same(r1 * W + c1, r2 * W + c2):
            print("Yes")
        else:
            print("No")
        flag = False
