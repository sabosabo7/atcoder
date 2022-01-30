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
# from math import gcd, comb, factorial
# from itertools import permutations, combinations, product


def cost(ha, hb):
    da = ha - hb
    if da >= 0:
        return da
    else:
        return da * 2


N, M = map(int, input().split())
H = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    wa = cost(H[A], H[B])
    wb = cost(H[B], H[A])
    G[A].append((B, wa))
    G[B].append((A, wb))
