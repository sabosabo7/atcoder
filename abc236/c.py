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

N, M = map(int, input().split())
S = input().split()
T = input().split()
i = 0

for s in S:
    if s in T:
        print("Yes")
    else:
        print("No")
