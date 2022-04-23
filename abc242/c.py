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


N = int(input())

ans = [[1] for _ in range(9)]
A = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
]


def mydot(X, Y):
    ni, nj = len(X), len(Y[0])
    ans = [[0] * nj for _ in range(ni)]
    for i in range(ni):
        for j in range(nj):
            tmp = 0
            for k in range(len(Y)):
                tmp += X[i][k] * Y[k][j]
            ans[i][j] = tmp
    return ans


def mymap(func, X):
    ni, nj = len(X), len(X[0])
    ans = [[0] * nj for _ in range(ni)]
    for i in range(ni):
        for j in range(nj):
            ans[i][j] = func(X[i][j])
    return ans


def matrixpow(base, exp, mod=None):
    if mod:
        func = lambda x: x % mod
    else:
        func = lambda x: x
    ni = len(base)
    ans = [[0] * ni for _ in range(ni)]
    for i in range(ni):
        ans[i][i] = 1
    tmp = base
    for s in bin(exp)[2:][::-1]:
        if s == "1":
            ans = mymap(func, (mydot(tmp, ans)))
        tmp = mymap(func, (mydot(tmp, tmp)))
    return ans


def mypow(base, exp, mod=None):
    if type(base) is list:
        return matrixpow(base, exp, mod)
    else:
        return pow(base, exp, mod)


ans = mydot(mypow(A, N - 1, MOD), ans)

print(sum(map(sum, ans)) % MOD)
