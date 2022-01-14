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
from itertools import permutations, combinations, product

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

l = 0
for i, j in combinations(range(N), 2):
    l = max(l, (P[i][0] - P[j][0]) ** 2 + (P[i][1] - P[j][1]) ** 2)

print(l ** 0.5)
