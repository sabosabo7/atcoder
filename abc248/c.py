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


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


N, M, K = map(int, input().split())


dp = mklist(N + 1, K + 50 + 1)
dp[0][0] = 1

for i in range(N):
    for j in range(K + 1):
        for add in range(1, M + 1):
            dp[i + 1][j + add] += (dp[i][j]) % MOD

print((sum(dp[-1][: K + 1])) % MOD)
