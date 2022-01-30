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
# from itertools import permutations, combinations, product

S = input()

for l in range(len(S)):
    if S[l] != "a":
        break
for r in range(len(S) - 1, -1, -1):
    if S[r] != "a":
        break

St = S[l : r + 1]
if l <= len(S) - 1 - r and St == St[::-1]:
    print("Yes")
else:
    print("No")
