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

A, B, C, X = map(int, input().split())

if X <= A:
    print(1)
elif X <= B:
    print(C / (B - A))
else:
    print(0)
