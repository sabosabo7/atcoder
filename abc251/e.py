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
A = list(map(int, input().split()))

dp = [INF] * (N + 10)
dp[0] = 0
for i, a in zip(range(1, N + 1), A):
    dp[i] = min(dp[i], dp[i - 1] + a)
    dp[i + 1] = min(dp[i + 1], dp[i - 1] + a)
ans = dp[N]

dp = [INF] * (N + 10)
dp[1] = A[-1]
for i, a in zip(range(1, N), A[:-1]):
    dp[i] = min(dp[i], dp[i - 1] + a)
    dp[i + 1] = min(dp[i + 1], dp[i - 1] + a)

ans = min(ans, dp[N - 1])

print(ans)
