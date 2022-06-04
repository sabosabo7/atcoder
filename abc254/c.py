from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter, defaultdict
# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd
# from itertools import permutations, combinations, product


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


N, K = map(int, input().split())
A = list(map(int, input().split()))

tmp = [[] for i in range(K)]
for i in range(N):
    tmp[i % K].append(A[i])

for i in range(K):
    tmp[i].sort()

t = 0
for i in range(N):
    if t > tmp[i % K][i // K]:
        print("No")
        exit()
    else:
        t = tmp[i % K][i // K]
else:
    print("Yes")
