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


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


N = int(input())

a = 10 ** 6
b = 0


def f(a, b):
    return (a + b) * (a ** 2 + b ** 2)


X = INF
while a >= 0 and b <= 10 ** 6:
    while f(a, b) >= N and a >= 0:
        X = min(X, f(a, b))
        a -= 1
    while f(a, b) < N:
        b += 1


print(X)
