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
S = input()

cnt = 0
dp = [[0] * 8 for _ in range(len(S) + 1)]

dp[0][0] = 1


for i in range(1, len(S) + 1):
    dp[i] = copy.deepcopy(dp[i - 1])
    if S[i - 1] == "a":
        dp[i][1] += dp[i - 1][0]
    elif S[i - 1] == "t":
        dp[i][2] += dp[i - 1][1]
    elif S[i - 1] == "c":
        dp[i][3] += dp[i - 1][2]
    elif S[i - 1] == "o":
        dp[i][4] += dp[i - 1][3]
    elif S[i - 1] == "d":
        dp[i][5] += dp[i - 1][4]
    elif S[i - 1] == "e":
        dp[i][6] += dp[i - 1][5]
    elif S[i - 1] == "r":
        dp[i][7] += dp[i - 1][6]

print(dp[-1][-1] % MOD)
