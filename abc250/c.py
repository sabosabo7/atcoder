from sys import exit, stdin, setrecursionlimit
from tkinter.messagebox import NO

from pyrsistent import v

from abc249.a import C

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


N, Q = map(int, input().split())


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,v):

    class Cell:
        def __init__(self):
            self.value = v
            self.prev = None
            self.next = None


class OrderedList:
    """
    swap(v1,v2) O(1)
    """

    def __init__(self, arr) -> None:
        self.val = {}
        self.pos = {}
        for p, v in arr:
            self.val[p] = v
            self.pos[v] = p

    def swap(self, x, y):
        px = self.pos[x]
        py = self.pos[y]
        self.val[px], self.val[py] = self.val[py], self.val[px]
        self.pos[x], self.pos[y] = self.pos[y], self.pos[x]

    def order(self):
        ans = []
        for _, a in sorted(self.val.items()):
            ans.append(a)
        return ans


D = OrderedList([i, i] for i in range(1, N + 1))

for _ in range(Q):
    x = int(input())
    idx = D.pos[x]
    if idx == N:
        D.swap(D.val[idx - 1], x)
    else:
        D.swap(x, D.val[idx + 1])

print(*D.order())
