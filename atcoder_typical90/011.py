from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
import copy

# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left


N = int(input())
Q = [list(map(int, input().split())) for _ in range(N)]

Q.sort()

dp = [[0] * 5001 for _ in range(N)]

for j in range(Q[0][0] - Q[0][1] + 1):
    dp[0][j + Q[0][1]] = Q[0][2]

for i in range(1, N):
    for j in range(5001):
        if Q[i][1] <= j <= Q[i][0]:
            dp[i][j] = max(dp[i - 1][j - Q[i][1]] + Q[i][2], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]


print(max(dp[-1]))
