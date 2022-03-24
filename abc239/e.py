from lib2to3.pytree import Node
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

N, Q = map(int, input().split())
X = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

S = [[] for _ in range(N)]
V = [True] * N


def dfs(G, i):
    global S
    global V
    V[i] = False
    tmp = []
    for n in G[i]:
        if V[n]:
            tmp.extend(dfs(G, n))
    tmp.append(X[i])
    tmp.sort(reverse=True)
    if len(tmp) > 20:
        tmp = tmp[:20]
    S[i] = tmp
    return S[i]


dfs(G, 0)


for _ in range(Q):
    v, k = map(int, input().split())
    v -= 1
    tmp = S[v]
    print(tmp[k - 1])
