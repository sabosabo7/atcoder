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

N, M, K, S, T, X = map(int, input().split())
S -= 1
T -= 1
X -= 1

G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

dp = [[[0, 0] for _ in range(N)] for _ in range(K + 1)]
dp[0][S][0] = 1

for k in range(1, K + 1):
    for i in range(N):
        if i == X:
            for j in G[i]:
                dp[k][i][0] += dp[k - 1][j][1]
                dp[k][i][1] += dp[k - 1][j][0]

        else:
            for j in G[i]:
                dp[k][i][0] += dp[k - 1][j][0]
                dp[k][i][1] += dp[k - 1][j][1]

        dp[k][i][0] %= MOD
        dp[k][i][1] %= MOD

print(dp[K][T][0])
