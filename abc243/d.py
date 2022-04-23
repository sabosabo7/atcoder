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
N, X = map(int, input().split())
S = input()

Q = []

for s in bin(X)[2:]:
    Q.append(s)

for s in S:
    if s == "U":
        Q.pop()
    elif s == "L":
        Q.append("0")
    else:
        Q.append("1")
ans = "".join(Q)
print(int(ans, 2))
