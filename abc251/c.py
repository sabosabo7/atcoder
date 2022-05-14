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


N = int(input())
submit = {}

for i in range(N):
    s, t = input().split()
    t = int(t)
    if not (s in submit):
        submit[s] = (t, -(i + 1))

ans = list(submit.values())
ans.sort(reverse=True)
print(ans[0][1] * (-1))
