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


N, W = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * (W + 1)

tmp = 0
for i in range(N):
    if A[i] <= W:
        cnt[A[i]] = 1


tmp = 0
for i in range(N):
    tmp += A[i]
    for j in range(i + 1, N):
        tmp += A[j]
        if tmp <= W:
            cnt[tmp] = 1
        tmp -= A[j]
    tmp -= A[i]

tmp = 0
for i in range(N):
    tmp += A[i]
    for j in range(i + 1, N):
        tmp += A[j]
        for k in range(j + 1, N):
            tmp += A[k]
            if tmp <= W:
                cnt[tmp] = 1
            tmp -= A[k]
        tmp -= A[j]
    tmp -= A[i]


print(sum(cnt))
