from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
# import copy
# input = stdin.readline

from collections import deque, Counter

# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))


Q = deque([])

for a in A:
    tmp = [0] * 10
    tmp[a] = 1
    Q.append(tmp)

while len(Q) > 1:
    Z = [0] * 10
    X = Q.popleft()
    Y = Q.popleft()
    for i in range(10):
        for j in range(10):
            Z[(i + j) % 10] += X[i] * Y[j]
            Z[(i + j) % 10] %= MOD
            Z[(i * j) % 10] += X[i] * Y[j]
            Z[(i * j) % 10] %= MOD
    Q.appendleft(Z)

for q in Q.pop():
    print(q)
