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
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for i in range(W):
    for j in range(H):
        print(A[j][i], end=" ")
    print()
