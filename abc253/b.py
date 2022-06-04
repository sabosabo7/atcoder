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


H, W = map(int, input().split())
D = []

for i in range(H):
    S = input()
    for j, s in enumerate(S):
        if s == "o":
            D.append((i, j))

ans = abs(D[0][0] - D[1][0]) + abs(D[0][1] - D[1][1])

print(ans)
