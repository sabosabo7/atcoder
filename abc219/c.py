from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

X = input()

x2a = {}
A = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
for a, x in zip(A, X):
    x2a[x] = a


N = int(input())
S = []
for _ in range(N):
    P = input()
    Q = ""
    for p in P:
        Q += x2a[p]
    S.append([Q, P])

S.sort()


for s in S:
    print(s[1])
