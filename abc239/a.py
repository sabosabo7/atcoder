from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# from bisect import bisect_left
import numpy as np

# from math import gcd
# from itertools import permutations, combinations, product


H = int(input())

print(np.sqrt(H * (12800000 + H)))
