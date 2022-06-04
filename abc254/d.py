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

cnt = 0
for i in range(1, N + 1):
    k = i
    j = 2
    while j ** 2 <= k:
        while k % (j ** 2) == 0:
            k //= j ** 2
        j += 1
    j = 1
    while k * j ** 2 <= N:
        cnt += 1
        j += 1


print(cnt)
