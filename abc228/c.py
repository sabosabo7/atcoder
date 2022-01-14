from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
from bisect import bisect_left, bisect_right

# import numpy as np
# from math import gcd, comb, factorial
# import itertools
N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

S = {}
for i, p in enumerate(P):
    S[i] = -1 * sum(p)

S1 = list(S.values())
S1.sort()

ans = [False] * N
for v in S.values():
    if v - 300 <= S1[K - 1]:
        print("Yes")
    else:
        print("No")
