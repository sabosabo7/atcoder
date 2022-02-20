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

D = 1

for i in range(N):
    a, b = map(int, input().split())
    D = (D << a) | (D << b)

if (D >> X) & 1:
    print("Yes")
else:
    print("No")
