from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np

# from math import gcd, comb, factorial
# from bisect import bisect_left

N = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * 3002
dp[A[0]] = 1
dp[B[0] + 1] = -1
tmp = 0
for i in range(3001):
    dp[i + 1] += dp[i]

for a, b in zip(A[1:], B[1:]):
    tmp_dp = [0] * 3002
    for i in range(b + 1):
        tmp_dp[max(i, a)] += dp[i]
        tmp_dp[b + 1] -= dp[i]
    tmp = 0
    for i in range(b + 1):
        tmp_dp[i + 1] += tmp_dp[i]
        tmp_dp[i + 1] %= MOD
    dp = tmp_dp
print(int(sum(dp[:-1]) % MOD))
