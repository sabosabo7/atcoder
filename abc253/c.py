from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter, defaultdict
# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd
# from itertools import permutations, combinations, product


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


class CrdComp:
    def __init__(self, raw=[]):
        self.rawlist = raw
        self._conv = {v: i for i, v in enumerate(sorted(set(self.rawlist)))}
        self._inv = dict(zip(self._conv.values(), self._conv.keys()))
        self.convlist = [map(self._conv, self.rawlist)]

    def add(self, x, update=False):
        self.rawlist.append(x)
        if update:
            self.update()

    def update(self):
        self._conv = {v: i for i, v in enumerate(sorted(set(self.rawlist)))}
        self._inv = dict(zip(self._conv.values(), self._conv.keys()))
        self.convlist = list(map(self.conv, self.rawlist))

    def conv(self, x):
        return self._conv[x]

    def inv(self, x):
        return self._inv[x]


Q = int(input())
cnv = CrdComp()
Que = []
for i in range(Q):
    q = list(map(int, input().split()))
    Que.append(q)
    if q[0] != 3:
        cnv.add(q[1])
cnv.update()


class BIT:
    """
    input param -> 0-indexed
    internal data structure -> 1-indexed
    """

    def __init__(self, n=10 ** 6):
        """
        n: data size
        """
        self.n = n
        self.d = [0] * (n + 1)

    def add(self, i, x):
        """
        i:0-indexed
        x:value
        """
        i += 1
        while i <= self.n:
            self.d[i] += x
            i += i & (-i)

    def sum(self, *i):
        """
        i:0-indexed
        sum(k): a0~ak
        sum(j,k): aj~ak
        """
        if len(i) == 1:
            i = i[0]
            x = 0
            i += 1
            while i > 0:
                x += self.d[i]
                i -= i & (-i)
            return x
        else:
            return self.sum(i[1]) - self.sum(i[0] - 1)

    def cum_sum(self):
        cum = []
        for i in range(self.n):
            cum.append(self.sum(i))
        return cum

    def lower_bound(self, x):
        """
        idx:0-indexed
        """
        idx = 0
        for i in range(self.n.bit_length(), 0, -1):
            tmp = idx + (1 << (i - 1))
            if (tmp <= self.n) and (self.d[tmp] < x):
                x -= self.d[tmp]
                idx += 1 << (i - 1)
        return idx


class BST:
    def __init__(self, n=10 ** 6):
        self.n = n + 1
        self.bit = BIT(self.n)
        self.cnt = 0

    def insert(self, x, d=1):
        self.bit.add(x, d)
        self.cnt += d

    def erase(self, x, d=1):
        self.insert(x, -d)

    def count(self, x):
        return self.bit.sum(x, x)

    def items(self):
        cnt = []
        for i in range(self.n):
            cnt += [i] * self.count(i)
        return cnt

    # def upper_bound(self, x):
    #     return self.bit.lower_bound(self.bit.sum(x))

    # def lower_bound(self, x):
    #     return self.bit.lower_bound(self.bit.sum(x - 1) + 1)

    def min(self, x=1):
        """
        return: x-th min
        """
        return self.bit.lower_bound(x)

    def max(self, x=1):
        """
        return: x-th max
        """
        return self.min(self.cnt - x + 1)


X = BST()

for q in Que:
    if q[0] == 1:
        x = q[1]
        X.insert(cnv.conv(x))
    elif q[0] == 2:
        x, c = q[1:]
        cnt = X.count(cnv.conv(x))
        X.erase(cnv.conv(x), min(cnt, q[2]))
    else:
        print(cnv.inv(X.max()) - cnv.inv(X.min()))
