from heapq import heapify
from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
import heapq

# from bisect import bisect_left
# import numpy as np
# from math import gcd, comb, factorial
# import itertools
N, K = map(int, input().split())
P = list(map(int, input().split()))

tmp = sorted(P[:K])
heapq.heapify(tmp)
print(tmp[0])

for i in range(K, N):
    heapq.heappushpop(tmp, P[i])
    print(tmp[0])
