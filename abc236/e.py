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
# from math import gcd, comb, factorial
# from itertools import permutations,combinations,product


def ismean(x):
    dp = [[0] * 2 for i in range(N)]
    dp[0][1] = A[0] - x
    for i in range(1, N):
        dp[i][0] = dp[i - 1][1]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + A[i] - x
    return max(dp[N - 1]) >= 0


def ismed(x):
    dp = [0] * N
    if A[0] >= x:
        dp[0] = 1
        f = True
    else:
        dp[0] = 0
        f = False
    for i in range(1, N):
        if A[i] >= x:
            dp[i] = dp[i - 1] + 1
            f = True
        else:
            if f:
                dp[i] = dp[i - 1]
                f = False
            else:
                dp[i] = dp[i - 1] - 1
                f = True
    return dp[N - 1] > 0


N = int(input())
A = list(map(int, input().split()))

mean = [0, 10 ** 9 + 1]

# for _ in range(50):
while mean[1] - mean[0] > 1e-3:
    tmp = (mean[0] + mean[1]) / 2
    if ismean(tmp):
        mean[0] = tmp
    else:
        mean[1] = tmp

print(mean[0])

med = [0, 10 ** 9 + 1]
while med[1] - med[0] > 1:
    tmp = (med[0] + med[1]) // 2
    if ismed(tmp):
        med[0] = tmp
    else:
        med[1] = tmp

print(med[0])
