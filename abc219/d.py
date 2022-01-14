from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

N = int(input())
X, Y = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]


dp = [[-1 * INF] * (X + 1) for _ in range(N + 1)]

dp[0][0] = 0

for c in C:
    x, y = c
    for n in range(N, 0, -1):
        for i in range(0, X + 1):
            dp[n][min(i + x, X)] = max(dp[n - 1][i] + y, dp[n][min(i + x, X)])


for n in range(1, N + 1):
    if dp[n][X] >= Y:
        print(n)
        exit()

print(-1)
