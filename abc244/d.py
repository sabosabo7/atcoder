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


S = input().split()
T = input().split()

S = "".join(S)
T = "".join(T)

C = {"RGB": 0, "BRG": 0, "GBR": 0, "RBG": 1, "BGR": 1, "GRB": 1}

if C[S] == C[T]:
    print("Yes")
else:
    print("No")
