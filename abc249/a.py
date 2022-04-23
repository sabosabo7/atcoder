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


A, B, C, D, E, F, X = map(int, input().split())


l_t = X // (A + C) * A * B
l_a = X // (D + F) * D * E

X_t = X % (A + C)
X_a = X % (D + F)
l_t += B * min(X_t, A)
l_a += E * min(X_a, D)


if l_t < l_a:
    print("Aoki")
elif l_t == l_a:
    print("Draw")
else:
    print("Takahashi")
