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
Q = int(input())
N = pow(2, 20)
A = [-1] * N
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = x
        while A[h % N] != -1:
            h += 1
        A[h % N] = x
    else:
        print(A[x % N])
