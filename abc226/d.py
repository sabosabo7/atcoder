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
from math import gcd, comb, factorial

# import itertools

N = int(input())
Vec = {}
City = []
x, y = map(int, input().split())
City.append((x, y))
for _ in range(N - 1):
    x, y = map(int, input().split())
    for x0, y0 in City:
        v1 = (x - x0, y - y0)
        v1 = (v1[0] // gcd(*v1), v1[1] // gcd(*v1))
        v2 = (x0 - x, y0 - y)
        v2 = (v2[0] // gcd(*v2), v2[1] // gcd(*v2))
        if not (v1 in Vec):
            Vec[v1] = 1
        if not (v2 in Vec):
            Vec[v2] = 1
    City.append((x, y))

ans = sum(list(Vec.values()))
print(ans)
