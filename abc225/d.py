from sys import exit, stdin, setrecursionlimit


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
class UnionFind_naive:
    """
    1-indexed
    """

    def __init__(self, n):
        self.D = [[-1, -1] for _ in range(n + 1)]

    def find_root(self, n):
        if self.D[n][0] == -1:
            return n
        else:
            return self.find_root(self.D[n][0])

    def find_leaf(self, n):
        if self.D[n][1] == -1:
            return n
        else:
            return self.find_leaf(self.D[n][1])

    def union(self, x, y):
        x_last = self.find_leaf(x)
        y_top = self.find_root(y)
        self.D[x_last][1] = y_top
        self.D[y_top][0] = x_last

    def disconnect(self, x, y):
        self.D[x][1] = -1
        self.D[y][0] = -1

    def member(self, n):
        top = self.find_root(n)
        mem = []
        mem.append(top)
        last = self.D[top][1]
        while last != -1:
            mem.append(last)
            last = self.D[last][1]
        return mem


N, Q = map(int, input().split())

C = UnionFind_naive(N)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, y = q[1], q[2]
        C.union(x, y)
    elif q[0] == 2:
        x, y = q[1], q[2]
        C.disconnect(x, y)
    else:
        x = q[1]
        mem = C.member(x)
        print(len(mem), *mem)
