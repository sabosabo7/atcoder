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

S = input()

cnt = 0

if S[0] == S[1]:
    cnt += 1
if S[0] == S[2]:
    cnt += 1
if S[1] == S[2]:
    cnt += 1

if cnt == 0:
    ans = 6
elif cnt == 1:
    ans = 3
else:
    ans = 1

print(ans)
