from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 998244353
INF = float('inf')
import copy
#input = stdin.readline

#from collections import deque, Counter
#import heapq
#from bisect import bisect_left
#import numpy as np
#from math import gcd, comb, factorial
#import itertools

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



N,M=map(int, input().split())
G =UnionFind(N)
C=[0]*N
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if C[A]>=2 or C[B]>=2:
        print("No")
        exit()
    else:
        C[A]+=1
        C[B]+=1
    if G.same(A,B):
        print("No")
        exit()
    else:
        G.union(A,B)
else:
    print("Yes")
    