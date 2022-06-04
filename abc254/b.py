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

ans = mklist(N, N)
for i in range(N):
    for j in range(N):
        if j == 0 or j == i:
            ans[i][j] = 1

for i in range(N - 1):
    for j in range(N - 1):
        ans[i + 1][j + 1] = ans[i][j] + ans[i][j + 1]

for i in range(N):
    print(*ans[i][: i + 1])
