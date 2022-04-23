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


N, P = map(int, input().split())
if N <= 2:
    print(0)
    exit()

dp = mklist(N + 1, N)
dp[1][2] = 26

for i in range(2, N + 1):
    dp[i] = copy.deepcopy(dp[i - 1])
    for k in range(2, N):
        dp[i][k] += (dp[i - 1][k - 2] * 25) % P

print(sum(dp[-1]) % P)
