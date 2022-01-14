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
# import itertools

H, W = map(int, input().split())

if H == 1 or W == 1:
    ans = H * W
else:
    ans = (1 + (H - 1) // 2) * (1 + (W - 1) // 2)
print(ans)
